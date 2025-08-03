symptom=str(input("Enter two syptoms:").strip().lower()
)
temp=int(input("What's your body temperature:"))
redflag=str(input("what's the red flag symptom:").strip().lower())
def symptom_checker(symptom, temp, redflag):
    diseases = {
        "Poisoning": {"puking", "tummy pain", "headache"},
        "Prego": {"cravings", "puking", "missed"},
        "Flu": {"puking", "bored", "running"}
    }

    temp_range = {
        range(-100, 0): "Freezing",
        range(0, 15): "Cold",
        range(15, 25): "Cool",
        range(25, 35): "Warm",
        range(35, 101): "Hot"
    }

    danger = {"convulsions", "not conscious", "blood", "fainting"}

    matched_disease = "not available"
    for disease in diseases:
        if symptom in diseases[disease]:
            matched_disease = disease
            break

    temp_label = "Unknown"
    for temp_band in temp_range:
        if temp in temp_band:
            temp_label = temp_range[temp_band]
            break

    redflag_alert = "safe"
    if redflag in danger:
        redflag_alert = "refer urgently"

    print("Disease:", matched_disease)
    print("Temperature Level:", temp_label)
    print("Red Flag Status:", redflag_alert)