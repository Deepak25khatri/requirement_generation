# # main.py

# import os
# from dotenv import load_dotenv
# from requirements_generator import RequirementsGenerator

# # Load environment variables
# load_dotenv()

# # Initialize RequirementsGenerator
# generator = RequirementsGenerator()

# def main():
#     domain = input("Enter the domain for requirement generation: ")
#     num_functional = int(input("Enter the number of functional requirements to generate: "))
#     num_non_functional = int(input("Enter the number of non-functional requirements to generate: "))

#     try:
#         functional, non_functional = generator.generate_requirements(domain, num_functional, num_non_functional)
        
#         print("\nFunctional Requirements:")
#         for i, req in enumerate(functional, 1):
#             print(f"{i}. {req}")

#         print("\nNon-Functional Requirements:")
#         for i, req in enumerate(non_functional, 1):
#             print(f"{i}. {req}")

#     except Exception as e:
#         print(f"An error occurred: {str(e)}")

#     # Collect feedback
#     feedback = input("Please rate the overall quality of the requirements (1-5): ")
#     comments = input("Any additional comments? ")

#     print(f"Feedback received: {feedback}/5")
#     print(f"Comments: {comments}")

# if __name__ == "__main__":
#     main()


#________________________________________________________________________________________


import os
from dotenv import load_dotenv
from requirements_generator import RequirementsGenerator

# Load environment variables
load_dotenv()

# Initialize RequirementsGenerator
generator = RequirementsGenerator()

def main():
    # Read SRS file content
    srs_file_path = input("Enter the path to the SRS markdown (.md) file: ")
    try:
        with open(srs_file_path, 'r') as file:
            srs_content = file.read()
    except FileNotFoundError:
        print(f"File not found: {srs_file_path}")
        return

    # Identify domain
    domain = generator.identify_domain(srs_content)
    print(f"Identified Domain: {domain}")

    num_functional = int(input("Enter the number of functional requirements to generate: "))
    num_non_functional = int(input("Enter the number of non-functional requirements to generate: "))

    try:
        functional, non_functional = generator.generate_requirements(domain, num_functional, num_non_functional)
        
        print("\nFunctional Requirements:")
        for i, req in enumerate(functional, 1):
            print(f"{i}. {req}")

        print("\nNon-Functional Requirements:")
        for i, req in enumerate(non_functional, 1):
            print(f"{i}. {req}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    # Collect feedback
    feedback = input("Please rate the overall quality of the requirements (1-5): ")
    comments = input("Any additional comments? ")

    print(f"Feedback received: {feedback}/5")
    print(f"Comments: {comments}")

if __name__ == "__main__":
    main()
