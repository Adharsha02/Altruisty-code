def find_strongest_trainees():
    # Input strength levels for 3 rounds
    print("Enter the strength levels (12 values):")
    strength_levels = [int(input()) for _ in range(12)]
    
    # Validate input
    if any(level < 1 or level > 200 for level in strength_levels):
        print("INVALID INPUT")
        return
    
    # Organize input into rounds for 4 trainees
    trainees = [strength_levels[i::4] for i in range(4)]
    
    # Calculate average strength for each trainee
    averages = [round(sum(trainee) / 3) for trainee in trainees]
    
    # Determine the highest average
    max_average = max(averages)
    
    # Check if all trainees are unfit
    if max_average < 100:
        print("All trainees are unfit")
        return
    
    # Identify trainees with the highest average
    strongest_trainees = [i + 1 for i, avg in enumerate(averages) if avg == max_average]
    
    # Output results
    for trainee in strongest_trainees:
        print(f"Trainee Number : {trainee}")

# Run the program
find_strongest_trainees()
