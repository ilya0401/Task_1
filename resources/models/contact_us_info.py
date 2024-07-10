from dataclasses import dataclass


@dataclass
class ContactUsInfo:
    full_name: str = None
    email: str = None
    company: str = None
    phone: str = None
    message: str = None
