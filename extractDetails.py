class Extract:
    """
    ----RedTron Python Development Team Tasks----

    Author : A S Adithiyaa
    Email : 1by20ai001@bmsit.in

    Description : Used for extracting the phone number and email details from any file type.
    
    Syntax : 
        >>> extract_object = Extract(<path_to_targetfile>)
        >>> return_holder1, return_holder2 = extract_object.get_details()

    Return value :
        return_holder1 will contain list of phone numbers.
        return_holder2 will contail list of emails.

    """


    def __init__(self, file_name):
        self.file_name = file_name
        self.phone_numbers = list()
        self.email_ids = list()
    

    def get_details(self):
        """
        Function to read the file contents and seperate the phone number and email.
        """

        f = open(self.file_name, "r")
        contents = f.read()
        contents = contents.split(",")

        for content in contents:
            content = content.strip()
            if "@" in content:
                self.email_ids.append(content)
            elif content.isdigit():
                self.phone_numbers.append(content)

        return (self.phone_numbers, self.email_ids)


if __name__ == "__main__":
    my_extract = Extract("./Data/extractDetails.txt")
    phones, emails = my_extract.get_details()
    print(phones)
    print(emails)