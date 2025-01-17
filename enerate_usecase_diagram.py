import os
import subprocess

def generate_use_case_diagram():
    # 1. Define the PlantUML diagram
    uml_text = r"""
@startuml

title "Online Shopping Portal - Use Case Diagram"

actor "Customer" as C

rectangle "Online Shopping Portal" {
    usecase "Visit Portal" as UC1
    usecase "Browse Products" as UC2
    usecase "Select Product" as UC3
    usecase "Add to Cart" as UC4
    usecase "View Cart" as UC5
    usecase "Edit Cart" as UC6
    usecase "Checkout" as UC7
    usecase "Register" as UC8
    usecase "Login" as UC9
    usecase "Make Payment" as UC10
    usecase "Confirm Shipment" as UC11
    usecase "Logout" as UC12
}

' -- Relationships --
C --> UC1 : "Starts Session"
C --> UC12 : "Ends Session"
UC1 --> UC2 : "Includes Browsing"
UC2 --> UC3 : "Includes (selecting item)"
UC3 --> UC4 : "Add to Cart"
UC4 --> UC5 : "View Cart"
UC5 --> UC6 : "Extends (if editing needed)"
UC6 --> UC5 : "Back to cart"
UC5 --> UC7 : "Proceed to Checkout"

' Register or Login to proceed (includes)
UC7 --> UC8 : "<<include>> (If New User)"
UC7 --> UC9 : "<<include>> (If Existing User)"

UC7 --> UC10 : "Make Payment"
UC10 --> UC11 : "Trigger Shipment Confirmation"

@enduml
"""

    # 2. Write the UML text to a .puml file
    puml_filename = "use_case_diagram.puml"
    with open(puml_filename, "w", encoding="utf-8") as f:
        f.write(uml_text)

    # 3. Use local PlantUML to generate a PNG
    #    (Make sure you have 'plantuml' command installed or specify the jar)
    try:
        subprocess.run(["plantuml", puml_filename], check=True)
        print("Diagram generated successfully: use_case_diagram.png")
    except FileNotFoundError:
        print("Error: 'plantuml' command not found. Install PlantUML or check your PATH.")
    except subprocess.CalledProcessError as e:
        print("Error generating diagram:", e)

if __name__ == "__main__":
    generate_use_case_diagram()
