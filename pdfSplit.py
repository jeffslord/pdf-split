from PyPDF2 import PdfFileReader, PdfFileWriter
import argparse
import sys
import os
import pyhdb
import time


def parse_args(args):
    parser = argparse.ArgumentParser(description='arguments')
    parser.add_argument('--pdf', '-p', help='path to pdf')
    parser.add_argument(
        '--dest', '-d', help='destination for split pages', default='/')
    return parser.parse_args(args)


def main(args):
    args = parse_args(args)
    pdf_file = open(args.pdf, 'rb')
    pdf_reader = PdfFileReader(pdf_file)
    page_numbers = pdf_reader.getNumPages()
    base_name = os.path.basename(args.pdf)
    base_name_ne = os.path.splitext(base_name)[0]

    # start_time = time.time()
    # connection = connect_hdb()
    # end_time = time.time()
    # print('[INFO] HDB Connection Time: ' + str(end_time - start_time))
    # cursor = connection.cursor()

    if not os.path.exists(args.dest):
        os.makedirs(args.dest)
    start_time = time.time()
    print('[INFO] Processing pdfs...')
    for i in range(page_numbers):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf_reader.getPage(i))
        new_page_path = os.path.join(
            args.dest, base_name_ne + '_page' + str(i + 1) + '.pdf')
        new_page = open(new_page_path, 'wb')
        pdf_writer.write(new_page)
    end_time = time.time()
    print('[INFO] PDF Processing Time: ' + str(end_time - start_time))
    print('[INFO] Time per page: ' +
          str((end_time - start_time) / page_numbers))
    print('[INFO] Pages per second: ' +
          str(page_numbers / (end_time - start_time)))

    # connection.close()


def connect_hdb():
    connection = pyhdb.connect(
        host="host",
        port=12345,
        user="user",
        password="pass"
    )
    return connection


if __name__ == '__main__':
    main(sys.argv[1:])
