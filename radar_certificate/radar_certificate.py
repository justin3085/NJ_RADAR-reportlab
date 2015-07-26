from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.lib.pagesizes import landscape
# from reportlab.platypus import Image




import csv

data_file = 'data.csv'

# Define a function to import data - which objects are being imported.


def import_data(data_file):
    attendee_data = csv.reader(open(data_file, "rt"))
    for row in attendee_data:
        # import the data
        agency_name = row[1]
        last_name = row[2]
        first_name = row[3]
        issue_date = row[4]
        exp_date = row[5]
        instructor = row[6]

        pdf_file_name = last_name + '_' + first_name + '.pdf'
        generate_certificate(agency_name, first_name, last_name, issue_date, exp_date, instructor, pdf_file_name)


# define a function to generate the certificate.  Puts the objects from file and uses reportlab to place.
def generate_certificate(agency_name, first_name, last_name, issue_date, exp_date, instructor, pdf_file_name):


    # ReportLab
    attendee_name = first_name + ' ' + last_name
    # Creates a canvas to work with.
    c = canvas.Canvas(pdf_file_name, pagesize=letter)

    # image - Image placement is by pixels - placed first as background image.

    sealSM = 'sealSM.jpg'
    c.drawImage(sealSM, 90, 620, width=140, height=140, mask=None)

    # header text
    c.setFont('Times-Roman', 12, leading=None)
    c.drawCentredString(160, 756, "STATE OF NEW JERSEY")

    c.setFont('Helvetica-Bold', 11, leading=None)
    c.drawCentredString(160, 740, agency_name)

    c.setFont('Times-Roman', 12, leading=None)
    c.drawCentredString(160, 724, "THIS IS TO CERTIFY THAT")

    c.setFont('Times-Roman', 12, leading=None)
    c.drawCentredString(160, 710, attendee_name)

    # static text
    c.setFont('Times-Roman', 11, leading=None)
    c.drawCentredString(160, 699, "has successfully completed the prescribed program")
    c.setFont('Times-Roman', 11, leading=None)
    c.drawCentredString(160, 686, "and is hereby authorized to be a")
    c.setFont('Times-Roman', 12, leading=None)
    c.drawCentredString(160, 668, "RADAR OPERATOR")

    # issue date static
    c.line(40, 647, 90, 647)
    c.setFont('Times-Roman', 8, leading=None)
    c.drawString(43, 637, "Issue Date")

    # add issue date
    c.setFont('Times-Roman', 11, leading=None)
    c.drawString(40, 649, issue_date)

    # expiration date static
    c.line(210, 647, 279, 647)
    c.setFont('Times-Roman', 8, leading=None)
    c.drawString(215, 637, "Expiration Date")

    # add expiration date
    c.setFont('Times-Roman', 11, leading=None)
    c.drawString(220, 649, exp_date)

    # add static instructor text
    c.line(100, 623, 225, 623)
    c.setFont('Helvetica', 8, leading=None)
    c.drawCentredString(160, 613, "Issuing Radar Instructor")

    # add instructor name signature
    pdfmetrics.registerFont(TTFont('ATCitadelScript', 'ATCitadelScript.ttf'))
    c.setFont('ATCitadelScript', 16, leading=None)
    c.drawCentredString(160, 625, instructor)

    # Add printed instructor name
    c.setFont('Times-Roman', 11, leading=None)
    c.drawCentredString(160, 602, instructor)

    # Add dotted cut line
    c.setDash(4, 3)
    c.line(0, 595, 290, 595)
    c.setDash(4, 3)
    c.line(290, 595, 290, 792)

    # Completes the page from above function, closes and starts a new page
    c.showPage()

    c.save()

import_data(data_file)
