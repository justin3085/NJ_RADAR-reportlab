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
        agency_name = row[0]
        last_name = row[1]
        first_name = row[2]
        issue_date = row[3]
        exp_date = row[4]
        instructor = row[5]

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

    #########################################################################################################################################

    # Bottom card
    c.setDash(4, 3)
    c.line(0, 382, 612, 382)

    sealSM = 'sealSM.jpg'
    c.drawImage(sealSM, 150, 32, width=315, height=315, mask=None)

    # header text
    c.setFont('Times-Roman', 24, leading=None)
    c.drawCentredString(310, 330, "STATE OF NEW JERSEY")

    c.setFont('Helvetica-Bold', 18, leading=None)
    c.drawCentredString(310, 303, agency_name)
    
    c.setFont('Times-Roman', 24, leading=None)
    c.drawCentredString(310, 268, "THIS IS TO CERTIFY THAT")

    c.setFont('Times-Roman', 36, leading=None)
    c.drawCentredString(310, 228, attendee_name)

    # static text
    c.setFont('Times-Roman', 20, leading=None)
    c.drawCentredString(310, 200, "has successfully completed the prescribed program")
    c.setFont('Times-Roman', 20, leading=None)
    c.drawCentredString(310, 175, "and is hereby authorized to be a")
    c.setFont('Times-Roman', 24, leading=None)
    c.drawCentredString(310, 142, "RADAR OPERATOR")

    # add static instructor text
    c.setDash(1)
    c.line(425, 50, 200, 50)
    c.setFont('Helvetica', 8, leading=None)
    c.drawCentredString(310, 40, "Issuing Radar Instructor")

    # pdfmetrics.registerFont(TTFont('ATCitadelScript', 'ATCitadelScript.ttf'))
    c.setFont('ATCitadelScript', 36, leading=None)
    c.drawCentredString(310, 55, instructor)

    # Add printed instructor name
    c.setFont('Times-Roman', 14, leading=None)
    c.drawCentredString(310, 28, instructor)

    # issue date static
    c.line(45, 100, 120, 100)
    c.setFont('Times-Roman', 14, leading=None)
    c.drawString(52, 88, "Issue Date")

    # add issue date
    c.setFont('Times-Roman', 14, leading=None)
    c.drawString(56, 103, issue_date)

    # expiration date static
    c.line(545, 100, 428, 100)
    c.setFont('Times-Roman', 14, leading=None)
    c.drawString(440, 88, "Expiration Date")

    # add expiration date
    c.setFont('Times-Roman', 14, leading=None)
    c.drawString(458, 103, exp_date)

    
    # Completes the page from above function, closes and starts a new page
    c.showPage()

    c.save()

import_data(data_file)
