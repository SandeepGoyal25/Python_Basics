from xml.sax.handler import feature_external_ges


filename = input("Enter the Filename: ")
f_extension = filename.split(".")
print("The extension of the file is: " + repr(f_extension[-1]))