# # requirements_generator.py

# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from langchain_cohere import ChatCohere
# from langchain_openai import ChatOpenAI
# from langchain_anthropic import ChatAnthropic
# from rules import FR_RULES, NFR_RULES

# class RequirementsGenerator:
#     def __init__(self):
#         self.llm = ChatOpenAI(model="gpt-4o-mini",temperature=0.8)

#     def _format_rules(self, rules):
#         formatted_rules = ""
#         for category, rule_list in rules.items():
#             formatted_rules += f"{category}:\n"
#             for rule in rule_list:
#                 formatted_rules += f"- {rule['rule']}\n  Description: {rule['description']}\n  Intuition: {rule['intuition']}\n"
#             formatted_rules += "\n"
#         return formatted_rules

#     def generate_requirements(self, domain, num_functional=5, num_non_functional=5):
#         fr_rules_text = self._format_rules(FR_RULES)
#         nfr_rules_text = self._format_rules(NFR_RULES)

#         requirement_prompt = PromptTemplate(
#             input_variables=["domain", "num_requirements", "req_type", "rules"],
#             template="Generate {num_requirements} {req_type} requirements for a {domain} system. "
#                      "Adhere to the following rules:\n\n{rules}\n\n"
#                      "Return the requirements as a numbered list. Requirements:"
#         )

#         fr_chain = LLMChain(llm=self.llm, prompt=requirement_prompt)
#         nfr_chain = LLMChain(llm=self.llm, prompt=requirement_prompt)

#         try:
#             functional_requirements = fr_chain.run(domain=domain, 
#                                                    num_requirements=num_functional, 
#                                                    req_type="functional",
#                                                    rules=fr_rules_text)
            
#             non_functional_requirements = nfr_chain.run(domain=domain, 
#                                                         num_requirements=num_non_functional, 
#                                                         req_type="non-functional",
#                                                         rules=nfr_rules_text)

#             # Process the output to return as lists
#             fr_list = functional_requirements.strip().split('\n')
#             nfr_list = non_functional_requirements.strip().split('\n')

#             # Remove numbering if present
#             fr_list = [req.split('. ', 1)[-1] for req in fr_list if req]
#             nfr_list = [req.split('. ', 1)[-1] for req in nfr_list if req]

#             return fr_list, nfr_list

#         except Exception as e:
#             print(f"An error occurred in generate_requirements: {str(e)}")
#             return [], []
        

#________________________________________________________________________________________

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_cohere import ChatCohere
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from rules import FR_RULES, NFR_RULES

class RequirementsGenerator:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.8)

    def _format_rules(self, rules):
        formatted_rules = ""
        for category, rule_list in rules.items():
            formatted_rules += f"{category}:\n"
            for rule in rule_list:
                formatted_rules += f"- {rule['rule']}\n  Description: {rule['description']}\n  Intuition: {rule['intuition']}\n"
            formatted_rules += "\n"
        return formatted_rules

    def identify_domain(self, srs_content):
        """Identify the domain based on the provided SRS content using LLM."""
        domain_prompt = PromptTemplate(
            input_variables=["srs_content"],
            template="Based on the following SRS content, identify the domain of the system. Provide a short description of the domain:\n\n{srs_content}\n\nDomain:"
        )
        domain_chain = LLMChain(llm=self.llm, prompt=domain_prompt)

        try:
            domain_description = domain_chain.run(srs_content=srs_content)
            return domain_description.strip()

        except Exception as e:
            print(f"An error occurred in identify_domain: {str(e)}")
            return "Unknown"

    def generate_requirements(self, domain, num_functional=5, num_non_functional=5):
        fr_rules_text = self._format_rules(FR_RULES)
        nfr_rules_text = self._format_rules(NFR_RULES)

        requirement_prompt = PromptTemplate(
            input_variables=["domain", "num_requirements", "req_type", "rules"],
            template="Generate {num_requirements} {req_type} requirements for a {domain} system. "
                     "Adhere to the following rules:\n\n{rules}\n\n"
                     "Return the requirements as a numbered list. Requirements:"
        )

        fr_chain = LLMChain(llm=self.llm, prompt=requirement_prompt)
        nfr_chain = LLMChain(llm=self.llm, prompt=requirement_prompt)

        try:
            functional_requirements = fr_chain.run(domain=domain, 
                                                   num_requirements=num_functional, 
                                                   req_type="functional",
                                                   rules=fr_rules_text)
            
            non_functional_requirements = nfr_chain.run(domain=domain, 
                                                        num_requirements=num_non_functional, 
                                                        req_type="non-functional",
                                                        rules=nfr_rules_text)

            # Process the output to return as lists
            fr_list = functional_requirements.strip().split('\n')
            nfr_list = non_functional_requirements.strip().split('\n')

            # Remove numbering if present
            fr_list = [req.split('. ', 1)[-1] for req in fr_list if req]
            nfr_list = [req.split('. ', 1)[-1] for req in nfr_list if req]

            return fr_list, nfr_list

        except Exception as e:
            print(f"An error occurred in generate_requirements: {str(e)}")
            return [], []

