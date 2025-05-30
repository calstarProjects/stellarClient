#!/usr/bin/env python3
import sys
import time
import os

IS_WINDOWS = sys.platform.startswith('win')

if IS_WINDOWS:
    import msvcrt
else:
    import tty
    import termios
    import select

class RawMode:
    """
    Context-manager to put Unix stdin into raw, no-echo mode for the duration,
    and restore the original settings on exit.
    """
    def __enter__(self):
        self.fd = sys.stdin.fileno()
        if not os.isatty(self.fd):
            raise RuntimeError("stdin is not a TTY. Use 'ssh -t' or allocate a pty.")
        self.orig_attrs = termios.tcgetattr(self.fd)
        tty.setraw(self.fd)  # raw = no-echo, no buffering
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self.orig_attrs)

def get_keys_unix(timeout=0.01, max_bytes=1024):
    """
    When stdin is ready, read up to max_bytes bytes at once.
    Returns a bytes object (may be empty).
    """
    rlist, _, _ = select.select([sys.stdin.fileno()], [], [], timeout)
    if rlist:
        return os.read(sys.stdin.fileno(), max_bytes)
    return b''

def get_keys_windows():
    """Drain and return all pending keypresses on Windows as a bytes object."""
    buf = b''
    while msvcrt.kbhit():
        buf += msvcrt.getch()
    return buf

def main():
    # Ensure stdout is unbuffered
    sys.stdout.reconfigure(line_buffering=True)

    os.write(sys.stdout.fileno(), b"Press any key (ESC to quit)...\n")

    try:
        if IS_WINDOWS:
            while True:
                data = get_keys_windows()
                for byte in data:
                    ch = chr(byte)
                    if ch == '\x1b':
                        return
                    os.write(sys.stdout.fileno(),
                             f"Key pressed: {ch!r}\n".encode())
                time.sleep(0.01)

        else:
            with RawMode():
                while True:
                    data = get_keys_unix()
                    if data:
                        for byte in data:
                            ch = chr(byte)
                            if ch == '\x1b':  # ESC
                                return
                            # Printable vs. control
                            if ch.isprintable():
                                out = f"Key pressed: {ch!r}\n"
                            else:
                                out = f"Key pressed: 0x{byte:02x}\n"
                            os.write(sys.stdout.fileno(), out.encode())
                    time.sleep(0.01)

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
