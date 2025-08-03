symptom=str(input("Enter two syptoms:").strip().lower()
)
def symptom_checker(symptom):
    diseases = {"Poisoning":{"Puking","Tummy pain","headache"},
                "Prego":{"Cravings","Puking","Missed"},
                "Flu":{"Puking","bored","running"}}
    for disease in diseases:
        if symptom in diseases[disease]:
            return disease
    return "not available"
print(symptom_checker(symptom))
    
