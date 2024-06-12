SUCCESS = 1

# Invalid input
INVALID_INPUT = 100
TOO_MANY_REQUEST = 101

# User
INVALID_LOGIN_TOKEN = 300
UNAUTHORIZED = 301
USER_NOT_FOUND = 302
INVALID_PASSWORD = 303
ADMIN_USER_NOT_FOUND = 304
APPLICATION_NOT_FOUND = 305
APPLICATION_ALREADY_SENT_TO_NBFC = 306
PHONE_ALREADY_EXISTS = 307
EMAIL_ALREADY_EXISTS = 308

# Business
BUSINESS_NOT_FOUND = 400

# Business document
DOCUMENT_NOT_FOUND = 401

# Promoter
PROMOTER_NOT_FOUND = 500

# OTP
OTP_VERIFICATION_FAILED = 600

# Decentro
DECENTRO_SERVER_ERROR = 700
INVALID_PAN = 701
INVALID_GSTIN = 702
INVALID_CIN = 703
INVALID_LLPIN = 704
INVALID_AADHAAR = 705
AADHAAR_NOT_FOUND = 706
AADHAAR_INACTIVE = 707

# documents
PDF_GENERATION_FAILURE = 800
DOCUMENT_ERROR = 801

# S3
S3_CLIENT_ERROR = 900

# Reference
REFERENCE_NOT_FOUND = 1000

# exotel
SMS_SEND_FAILED = 1100


error_messages = {
    INVALID_INPUT: 'Invalid input',
    TOO_MANY_REQUEST: 'Too many requests',
    INVALID_LOGIN_TOKEN: 'Invalid token for login',
    UNAUTHORIZED: "Unauthorized",
    # BORROWER_NOT_FOUND: "User not found",
    INVALID_PASSWORD: "Invalid password",
    USER_NOT_FOUND: 'user not found',
    # BUSINESS_NOT_FOUND: "Business not found",
    # PROMOTER_NOT_FOUND: "Promoter not found",
    # DOCUMENT_NOT_FOUND: "Document not found",
    # ADMIN_USER_NOT_FOUND: "Admin user not found",
    # OTP_VERIFICATION_FAILED: "OTP verification failed",
    # DECENTRO_SERVER_ERROR: "Decentro server error",
    # INVALID_PAN: "Invalid PAN",
    # INVALID_GSTIN: "Invalid GSTIN",
    # INVALID_CIN: "Invalid CIN",
    # INVALID_LLPIN: "Invalid LLPIN",
    # INVALID_AADHAAR: "Invalid Aadhar",
    # AADHAAR_NOT_FOUND: "Aadhar not found",
    # AADHAAR_INACTIVE: "Aadhar inactive",
    # PDF_GENERATION_FAILURE: "PDF generation failure",
    # S3_CLIENT_ERROR: "S3 client error",
    # DOCUMENT_ERROR: "Error while creating documents",
    # APPLICATION_NOT_FOUND: "User has not confirmed their details",
    # APPLICATION_ALREADY_SENT_TO_NBFC: "Application already sent to NBFC",
    # PHONE_ALREADY_EXISTS: "User already exists with this phone number",
    EMAIL_ALREADY_EXISTS: "User already exists with this email",
    # REFERENCE_NOT_FOUND: "Reference not found",
    # SMS_SEND_FAILED: "Failed to send SMS"
}
