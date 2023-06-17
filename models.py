from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship



class Company(Base):
    """This Table represent the Company"""

    __tablename__ = "company"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = String(String)
    role = Column(String, default='comapny')
    is_active = Column(Boolean, default=True)

    employee = relationship("Employee", back_populates="company")


class Employee(Base):
    """This table contain all employees"""


    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String, unique=True)
    password = String(String)
    role = Column(String, default='employee')
    is_active = Column(Boolean, default=True)

    company_id = Column(Integer, ForeignKey('company.id'))

    company = relationship("Company", back_populates="employee") # relationship with company
    chat = relationship("Chat", back_populates='employee')  # relationship to chat



class Chat(Base):
    """This table contains the all chats of an employee"""

    __tablename__ = 'chats'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)

    employee_id = Column(Integer, ForeignKey('employees.id'))

    employee = relationship('Employee', back_populates='chat')

    conversation = relationship('Conversation', back_populates='chat')


class Conversation(Base):
    """This table contain the conversation between employee and chatbot"""

    __tablename__ = 'conversations'

    id = Column(Integer, primary_key=True, index=True)
    req = Column(String)
    res = Column(String)
    
    chat_id = Column(Integer, ForeignKey('chats.id'))
    chat = relationship('Chat', back_populates='conversation')
