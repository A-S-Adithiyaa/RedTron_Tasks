import re
import textract
import PyPDF2 


class Extract:
    """
    ----RedTron Python Development Team Tasks----

    Author : A S Adithiyaa
    Email : 1by20ai001@bmsit.in

    Description : Used for extracting all phone numbers and email details from any file type.
    
    Syntax : 
        >>> extract_object = Extract(<path_to_targetfile>)
        >>> return_holder1, return_holder2 = extract_object.get_details()

    Return value :
        return_holder1 will contain list of phone numbers.
        return_holder2 will contail list of emails.

    """


    def __init__(self, file_name):
        self.file_name = file_name
        self.text = str()
        self.phone_numbers = list()
        self.email_ids = list()
    

    def get_contents(self):
        if (self.file_name.endswith(".pdf")):
            pdfFileObj = open(self.file_name, 'rb') 
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
            pages = pdfReader.numPages
            for page in range(pages):
                pageObj = pdfReader.getPage(page) 
                self.text += pageObj.extractText()
        else:
            self.text = textract.process(self.file_name)
            self.text = self.text.decode("utf-8") 


    def get_details(self):
        """
        Function to read the file contents and seperate the phone number and email.
        """

        self.get_contents()

        IndianNumber = re.compile(r'''(
        ([+]\d{1,2})
        (\d{3,10})
        )''',re.VERBOSE)

        phoneRegex = re.compile(r'''((\d{3}|\(\d{3}\))?(\s|-|\.)(\d{3})(\s|-|\.)(\d{4})(\s*(ext|x|ext.)\s*(\d{2,5}))?)''', re.VERBOSE)

        emailRegex = re.compile(r'''([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))''', re.VERBOSE)


        phone_groups = phoneRegex.findall(self.text)
        email_groups = emailRegex.findall(self.text)
        Indian_Contacts = IndianNumber.findall(self.text)

        for group in phone_groups:
            self.phone_numbers.append(group[0])

        for group in Indian_Contacts:
            if group[1] == '+91':
                phoneNum = group[1] + group[2]
            self.phone_numbers.append(phoneNum)

        for group in email_groups:
            self.email_ids.append(group[0])

        return (self.phone_numbers, self.email_ids)


if __name__ == "__main__":
    files = ["extractDetails.pdf", "extractDetails.csv", "extractDetails.xls", "extractDetails.docx", "extractDetails.json", "extractDetails.txt", "extractDetails.html"]
    for file in files:
        my_extract = Extract("./Data/" + file)
        phones, emails = my_extract.get_details()
        print(phones)
        print(emails)
