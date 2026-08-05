# Class Variable: company_name = "AIForge Labs"

# Class Method: show_company()

# Print the company name.



class Company:

    company_name = "AIForge Labs"


    @classmethod
    def show_company(cls):
        return cls.company_name

print(Company.show_company())