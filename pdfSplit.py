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
        '--dest', '-d', help='destination for split pages', default='split')
    return parser.parse_args(args)


def main(args):
    # Parse the arguments passed from command line
    args = parse_args(args)
    # Call split function
    split_pdf(args.pdf, args.dest)


def split_pdf(pdf_path, destination):
    """Function to split a single pdf into single page pdfs."""
    # Open the pdf specified by the pdf argument
    pdf_file = open(pdf_path, 'rb')
    # Open pdf with PdfFileReader
    pdf_reader = PdfFileReader(pdf_file)
    # Get number of pages
    page_numbers = pdf_reader.getNumPages()
    # This gets the "pdf_name.pdf" from the path given
    file_folder = os.path.basename(os.path.normpath(pdf_path))
    # This removes the .pdf so it just has the name of the pdf (not really necessary)
    file_folder = os.path.splitext(file_folder)[0]
    # Make path for split pages (the pages will be in a folder named whatever the pdf name is)
    path = os.path.join(destination, file_folder)
    print('[INFO] Split page output path: ' + path)
    # If the destination for split pages does not exist, create it (else an error will occur)
    if not os.path.exists(path):
        os.makedirs(path)
        print("Creating path {0}".format(path))
    # Start timer
    start_time = time.time()
    print('[INFO] Processing pdfs...')
    print('[INFO] Pages found: {0}'.format(page_numbers))
    # Loop the number of pages in pdf
    for i in range(page_numbers):
        # Create pdf writer object
        pdf_writer = PdfFileWriter()
        # Add single pdf page based on loop index
        pdf_writer.addPage(pdf_reader.getPage(i))
        # Make path for storing split page
        new_page_path = os.path.join(
            path, 'page_' + str(i + 1) + '.pdf')
        print('[INFO] Processing: {0}'.format(new_page_path))
        # Open new file at path of new split page
        new_page = open(new_page_path, 'wb')
        # Write file to the split page path
        pdf_writer.write(new_page)
    # Stop timer
    end_time = time.time()
    print('[INFO] PDF Processing Time: {0}'.format(str(end_time - start_time)))
    print('[INFO] Time per page: {0}'.format(
          str((end_time - start_time) / page_numbers)))
    print('[INFO] Pages per second: {0}'.format(
          str(page_numbers / (end_time - start_time))))


def connect_hdb():
    """Connect to Hana Database and return the connection object."""
    connection = pyhdb.connect(
        host="host",
        port=12345,
        user="user",
        password="pass"
    )
    return connection


if __name__ == '__main__':
    main(sys.argv[1:])
