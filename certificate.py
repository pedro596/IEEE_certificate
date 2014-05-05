#!/usr/bin/env python
# -*- coding: utf8 -*-

# ------------------------------------------------------ #
#  Certificate Generator - Version:1.0.1 Date: 4/May/14  #
#  --------- Specially designed to ISEPinIEEE ---------- # 
#  This module have one funtion > createCertificate      #
#  Author: Victor Fernandes | victorfern91[at]gmail.com  #
#							        Language: Python 2.7 #
# ------------------------------------------------------ #

# imports
import hashlib # md5 

from fpdf import FPDF # fpdf

def createCertificate(
	workshop_name,
	workshop_day,
	workshop_month,
	workshop_year,
	workshop_speaker,
	student_name,
	student_mail,
	chair_IEEE
	):
	
	l_name = unicode( student_name, "utf-8" )
	w_name = unicode( workshop_name, "utf-8" )
	c_name = unicode( chair_IEEE, "utf-8" )
	s_name = unicode( workshop_speaker, "utf-8" )

	# PDF File Properties
	pdf=FPDF('L','mm','A4')
	pdf.set_margins(left=0,top=0,right=0)
	pdf.set_auto_page_break(False,margin=0)
	pdf.add_page()
	# ISEPinIEEE Logo
	pdf.set_font('Arial','',30)
	pdf.cell(297,40,'',0,1,'C')#fill=True
	pdf.image('logos/isepinieee_logo.jpg',190,5, 0,35,'','')
	# Workshop Title
	pdf.set_text_color(0,102,153)
	pdf.cell(293,20,w_name,0,1,'R')
	# Cetificate Bar
	pdf.set_fill_color(0,102,153)
	pdf.set_text_color(255,255,255)
	pdf.set_font('Arial','',48)
	pdf.cell(297,35,'Certificate',0,1,'C',fill=True)
	pdf.cell(297,10,'',0,1,'C')
	# Certificate Text
	pdf.set_font('Arial','',20)
	pdf.set_text_color(0,0,0)
	# This pdf element is used to center ( Note: (297-240)/2 = 28.5)
	pdf.cell(19,20,'',0,0,'C')
	pdf.multi_cell(259,12.5, 'We certifiy that '+l_name+' participated in the talk \"'+w_name+'\", organized by the ISEPinIEEE.',0,1,'C')
	#MultiCell( 200, 40, $reportSubtitle, 1);
	# Certificate Date
	pdf.cell(297,10,'',0,1,'C')
	pdf.cell(19,15,'',0,0,'C')
	pdf.cell(240,10,'Porto, '+workshop_month+' '+str(workshop_day)+', '+str(workshop_year),0,1,'L')

	#Speaker & Chair Signature
	pdf.image(workshop_name+'/signatures/Speaker.jpg',157,166, 60, 17,'','')
	pdf.image(workshop_name+'/signatures/chair.jpg',230,166, 60, 17,'','')

	#Speaker & Chair
	pdf.set_font('Arial','',18)
	pdf.cell(150,20,'',0,0,'C')
	pdf.cell(73.5,20,'Speaker',0,0,'C')
	pdf.cell(73.5,20,'Chair',0,1,'C')
	pdf.cell(150,35,'',0,0,'C')
	pdf.cell(73.5,35,s_name,0,0,'C')
	pdf.cell(73.5,35,c_name,0,1,'C')

	#SpeakerLine & ChairLine
	pdf.line(155, 180, 218, 180)
	pdf.line(228, 180, 292, 180)
	# IEEE and ISEP logos
	pdf.image('logos/ieee_logo.jpg',20,175, 0, 17,'','')
	pdf.image('logos/isep_logo.jpg',85,175, 0, 17,'','')
	# Save PDF File
	certificate_name = hashlib.md5(student_mail)
	pdf.output(workshop_name+'/'+certificate_name.hexdigest()+'.pdf','F')

if __name__ == '__main__':
	createCertificate("Python Workshop", 3, '<MONTH>', 2014, '<SPEAKER NAME>', '<STUDENT NAME>', 'test@ieee.dee.isep.ipp.pt','<CHAIR NAME>')