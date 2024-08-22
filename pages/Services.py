import streamlit as st


# Function to create dropdowns with multiple mental health resources
def display_resources(college_Name, services):
    with st.expander(f"{college_Name}", expanded=False):
        for service in services:
            st.markdown(f"**Service Name:** {service['Name']}")
            st.markdown(f"**Email:** {service['Email']}")
            st.markdown(f"**Phone Number:** {service['Phone']}")
            st.markdown(f"**Website:** [Link]({service['Website']})")
            st.markdown("---")


# Insert containers separated into tabs:
tab1, tab2, tab3 = st.tabs(["Community Colleges", "Bachelors Colleges", "Master Colleges"])

# Tab 1 content
with tab1:
    
    display_resources("Bronx Community College", [
        {"Name": "Office of Personal Counseling",
         "Email": "Personal.Counseling@bcc.cuny.edu", "Phone": "(718)-289-5223", "Website": "https://www.bcc.cuny.edu/campus-resources/personal-counseling-services/"},
        {"Name": "Health Services",
         "Email": "healthservices@bcc.cuny.edu", "Phone": "(718)-289-5858", "Website": "https://www.bcc.cuny.edu/campus-resources/health-services/"}
    ])

    display_resources("Hostos Community College", [
        {"Name": "Counseling Services",
         "Email": "infocounseling@hostos.cuny.edu", "Phone": "(718)-518-4461", "Website": "https://www.hostos.cuny.edu/Administrative-Offices/SDEM/Counseling-Services"},
        {"Name": "The Health and Wellness Center",
         "Email": "usanders@hostos.cuny.edu", "Phone": "(718)-518-4444", "Website": "https://www.hostos.cuny.edu/Administrative-Offices/SDEM/Health-and-Wellness-Center/Helpful-Health-and-Wellness-Websites"}
    ])

    display_resources("Kingsborough Community College", [
        {"Name": "Counseling Center",
         "Email": "Counseling.Center@kbcc.cuny.edu", "Phone": "(718)-368-5975", "Website": "https://www.kbcc.cuny.edu/sws/counseling-center.html"},
        {"Name": "Health Center",
         "Email": "Health.Center@kbcc.cuny.edu",
         "Phone": "(718)-368-5684",
         "Website": "https://www.kbcc.cuny.edu/healthservices/index.html"
         }
    ])

    display_resources("Borough of Manhattan Community College", [
        {"Name": "Counseling Center",
         "Email": "counselingcenter@bmcc.cuny.edu",
         "Phone": "(212)-220-8140",
         "Website": "https://www.bmcc.cuny.edu/student-affairs/counseling/"},
        {"Name": "Health Services",
         "Email": "healthservices@bmcc.cuny.edu",
         "Phone": "(212)-220-8256",
         "Website": "https://guttman.cuny.edu/students/counseling-and-wellness-center/"}
    ])

    display_resources("Guttman Community College", [
        {"Name": "Counseling and Wellness Center",
         "Email": "Counseling.wellness@guttman.cuny.edu",
         "Phone": "(646)-313-8026",
         "Website": "https://guttman.cuny.edu/students/counseling-and-wellness-center/"}
    ])

    display_resources("LaGuardia Community Collegee", [
        {"Name": "The Wellness Center",
         "Email": "WellnessCenter@lagcc.cuny.edu",
         "Phone": "(718)-482-5471",
         "Website": "https://www.laguardia.edu/students/the-wellness-center/"},
        {"Name": "Mental Health and Counseling",
         "Email": "dbayrakdar@lagcc.cuny.edu",
         "Phone": "(718)-482-7200",
         "Website": "https://www.laguardia.edu/mental-health-and-counseling-experts/"}
    ])

    display_resources("Queensborough Community College", [
        {"Name": "Counseling Center",
         "Email": "Counseling@qcc.cuny.edu",
         "Phone": "(718)-6316370",
         "Website": "https://www.qcc.cuny.edu/counseling/index.html"},
        {"Name": "Office of Health Services", "Email": "HealthServices@qcc.cuny.edu", "Phone": "(718)-631-6375", "Website": "https://www.qcc.cuny.edu/healthServices/"}
    ])
tab1.markdown('---')

#tab 2 writing
with tab2:
        display_resources("Lehman College", [
        {"Name": "Counseling Center",
         "Email": "counseling.center@lehman.cuny.edu",
         "Phone": "(718)-960-8761",
         "Website": "https://www.lehman.edu/counseling-center/"},
        {"Name": "Student Health Center", 
         "Email": "med.requirements@lehman.cuny.edu",
         "Phone": "(718)-960-8909",
         "Website": "med.requirements@lehman.cuny.edu"        
        }
    ])
        

        display_resources("Brooklyn College", [
        {"Name": "Personal Counseling",
         "Email": "BCPersonalCounseling@gmail.com",
         "Phone": "NA",
         "Website": "https://www.brooklyn.edu/dosa/health-and-wellness/personal-counseling/"}
    ])

        display_resources("Medgar Evans College", [
        {"Name": "Counseling & Psychological Services",
         "Email": "cap@mec.cuny.edu",
         "Phone": "(973) 946-8120",
         "Website": "https://www.mec.cuny.edu/student-success/counseling-psychological-services/"}
    ])

        display_resources("Baruch College", [
        {"Name": "Counseling Center",
         "Email": "counseling@baruch.cuny.edu",
         "Phone": "(646)-312-2155",
         "Website": "https://studentaffairs.baruch.cuny.edu/health/topics/mentalhealth/"}
    ])

        display_resources("City Tech", [
        {"Name": "Counseling Center",
         "Email": "counseling@citytech.cuny.edu",
         "Phone": "(718)-260-5030",
         "Website": "https://www.citytech.cuny.edu/counseling/"}
    ])

        display_resources("The City College of New York", [
        {"Name": "Counseling Center",
         "Email": "counseling@ccny.cuny.edu",
         "Phone": "(212) 650-8222",
         "Website": "https://www.ccny.cuny.edu/counseling?srsltid=AfmBOorhZ9F9T05zdxGxItHo7Sx5SMDBX-QlJK9yQye1Vl6KyCaXFJ--"}
    ])

        display_resources("Hunter College", [
        {"Name": "Counseling Services",
         "Email": "personalcounseling@hunter.cuny.edu",
         "Phone": "(212)-772-4931",
         "Website": "https://hunter.cuny.edu/students/health-wellness/counseling-and-wellness-services/counseling-services/"}
    ])
        
        display_resources("John Jay College", [
        {"Name": "Counseling Services Center",
         "Email": "NA",
         "Phone": "(212)-237-8111",
         "Website": "https://www.jjay.cuny.edu/student-life/wellness-center/counseling-services-center"}
    ])

        display_resources("Macaulay Honors College", [
        {"Name": "Mental Health and Wellness Center",
         "Email": "wellness@mhc.cuny.edu",
         "Phone": "NA",
         "Website": "https://macaulay.cuny.edu/student-life/student-well-being/mental-health-and-wellness-center/"}
    ])

        display_resources("Queens College", [
        {"Name": "Counseling Services",
         "Email": "CounselingServices@qc.cuny.edu",
         "Phone": "718-997-5420",
         "Website": "https://www.qc.cuny.edu/cs/"}
    ])

        display_resources("York College", [
        {"Name": "Student Health Services Center",
         "Email": "StudHealthSvcCtr@york.cuny.edu",
         "Phone": "718-997-5420",
         "Website": "https://www.qc.cuny.edu/cs/"}
    ])

        display_resources("College of Staten Island", [
        {"Name": "Health and Wellness Services",
         "Email": "healthcenter@csi.cuny.edu",
         "Phone": "718-982-3045",
         "Website": "https://www.csi.cuny.edu/campus-life/student-services/health-and-wellness-services"}
    ])
tab2.markdown('---')

#tab 3 writing
#tab3.markdown('--- \n#### Craig Newmark Graduate School of Journalism')
with tab3:

        display_resources("CUNY Graduate Center", [
        {"Name": "Student Counseling Services",
         "Email": "wellness@gc.cuny.edu",
         "Phone": "212-817-7020 ",
         "Website": "https://www.gc.cuny.edu/student-counseling-services"}
    ])
        
        display_resources("CUNY SPH", [
        {"Name": "Counseling and Wellness Services",
         "Email": "sherry.adams@sph.cuny.edu",
         "Phone": "(646)-364-9526",
         "Website": "https://sph.cuny.edu/students/student-services/student-wellness/counseling-and-wellness-services/?_gl=1*ugi2ss*_up*MQ..*_ga*NDA3NzY2MDc1LjE3MjQzNTI1OTE.*_ga_6XD2NXSRSN*MTcyNDM1MjU4OC4xLjAuMTcyNDM1MjU4OC4wLjAuMA.."}
    ])
        
        display_resources("School of Labor and Urban Studies", [
        {"Name": "Counseling and Wellness",
         "Email": "Lindsay.kazi@slu.cuny.edu",
         "Phone": "NA",
         "Website": "https://slu.cuny.edu/academic-affairs/student-affairs/student-services/counseling-wellness/"}
    ])
        
        display_resources("School of Professional Studies", [
        {"Name": "Student Counseling Services",
         "Email": "counseling@sps.cuny.edu",
         "Phone": "(646)-664-8647",
         "Website": "https://sps.cuny.edu/student-services/student-counseling-services"}
    ])

        display_resources("School of Law", [
        {"Name": "Counseling and Mental Health Services",
         "Email": "mentalwellness@law.cuny.edu",
         "Phone": "(718)-340-4207",
         "Website": "https://www.law.cuny.edu/students/health-wellness/counseling-and-mental-health-services/"}
    ])
tab3.markdown('---')
