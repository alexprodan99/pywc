import argparse
import locale
import os
import sys
from typing import Union
from io import BytesIO, BufferedReader

def parse_args():
    parser = argparse.ArgumentParser(description="Custom implementation for wc")
    parser.add_argument("-c", required=False, action="store_true", help="Number of bytes")
    parser.add_argument("-l", required=False, action="store_true", help="Number of lines")
    parser.add_argument("-w", required=False, action="store_true", help="Number of words")
    parser.add_argument("-m", required=False, action="store_true", help="Number of characters")
    parser.add_argument("path", nargs="?", default=None, help="File path")
    return parser.parse_args()

def count_bytes(file_stream: Union[BytesIO, BufferedReader]) -> str:
    """Count and return number of bytes"""
    file_stream.seek(0, os.SEEK_END)
    wbytes = file_stream.tell()
    file_stream.seek(0)
    return str(wbytes)

def count_lines(file_stream: Union[BytesIO, BufferedReader]) -> str:
    """Count and return number of bytes"""
    file_stream.seek(0)
    lines = sum(
        buf.count(b"\n") for buf in iter(lambda: file_stream.read(1024 * 1024), b"")
    )
    return str(lines)

def count_multibytes(file_stream: Union[BytesIO, BufferedReader]) -> str:
    """Count and return number of multibytes"""
    current_locale_encoding = locale.getpreferredencoding()
    file_stream.seek(0)
    multibytes = file_stream.read()
    multibytes = multibytes.decode(current_locale_encoding)
    return str(len(multibytes))

def count_words(file_stream: Union[BytesIO, BufferedReader]) -> str:
    """Count and return number of words"""
    file_stream.seek(0)
    words = file_stream.read().decode()
    return str(len(words.split()))


def handle(args, file_stream: Union[BytesIO, BufferedReader]):
    handlers = []

    if args.c:
        handlers.append(count_bytes)
    
    if args.l:
        handlers.append(count_lines)
    
    if args.m:
        handlers.append(count_multibytes)
    
    if args.w:
        handlers.append(count_words)
    
    if not any([args.c, args.l, args.w, args.m]):
        handlers = [
            count_lines,
            count_words,
            count_bytes,
        ]
    
    return [handler(file_stream) for handler in handlers]

if __name__ == "__main__":
    args = parse_args()
    
    if args.path:
        path = args.path
        with open(path, "rb") as f:
            std_out = handle(args, f)
            std_out.append(str(path))
            print("\t".join(std_out))
    else:
        stdin_data = sys.stdin.buffer.read()
        stdin_buffer = BytesIO(stdin_data)
        std_out = handle(args, stdin_buffer)
        print("\t".join(std_out))
