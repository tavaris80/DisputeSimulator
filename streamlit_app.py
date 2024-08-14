import random

# Define stop words manually (since NLTK might not be available in all environments)
stop_words = {'ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than'}

def get_random_dispute_scenario():
    """Fetches a random dispute scenario from PDS documents with customer dialogues and ideal responses"""

    # Scenarios, customer dialogues, ideal responses, and keywords extracted from PDS
    scenarios = [
        # Scenario 1: Water damage claim denied due to pre-existing condition (from Contents Insurance for Strata PDS)
        ("Water damage claim denied due to pre-existing condition.",
         "I can't believe you're denying my claim! This water damage is new, not pre-existing!",
         "I understand your frustration, Mr./Ms. [Customer Name]. Let's review the policy details together to clarify what constitutes a pre-existing condition. If the damage is indeed new, we'll certainly reassess your claim.",
         ["review", "policy", "pre-existing", "reassess"], "angry"),

        # Scenario 2: Dispute over the definition of 'common property' in a claim (from Residential Strata Insurance Plan PDS)
        ("Dispute over the definition of 'common property' in a claim.",
         "I don't understand why this isn't covered. It's in the hallway, so it's clearly common property!",
         "You're right, the hallway is generally considered common property. However, let's double-check the specific bylaws and definitions in your strata plan to ensure there are no exceptions in your case.",
         ["clarify", "common property", "bylaws", "exceptions"], "confused"),

        # Scenario 3: Claimant disagrees with the assessed value of damaged property (from Landlords Insurance for Strata PDS)
        ("Claimant disagrees with the assessed value of damaged property.",
         "The amount you're offering is way too low! My furniture was practically new!",
         "I understand your concern about the assessed value. We base our assessments on fair market value, considering depreciation. However, if you have evidence that supports a higher value, such as receipts or appraisals, we're happy to review it.",
         ["assessed value", "market value", "depreciation", "evidence", "review"], "disappointed"),

        # Scenario 4: Delay in claim processing causing frustration (from Commercial Strata Insurance Plan PDS)
        ("Delay in claim processing causing frustration for the claimant.",
         "I've been waiting for weeks! When will my claim be processed? This is unacceptable!",
         "I apologize for the delay and any inconvenience it has caused. I understand your frustration. I'll personally escalate your claim to ensure it's processed as quickly as possible. You'll receive regular updates on its progress.",
         ["apologize", "delay", "escalate", "updates"], "frustrated"),

        # Scenario 5: Claimant's property was damaged during a neighbor's renovation (from any PDS, general scenario)
        ("Claimant's property was damaged during a neighbor's renovation.",
         "My neighbor's renovation caused a pipe to burst, flooding my unit! Why isn't this covered?",
         "I'm sorry to hear about the damage to your unit. Let's review your policy to see if damage caused by a neighbor's renovation is covered. If it is, we'll initiate the claims process and guide you through the next steps.",
         ["neighbor", "renovation", "damage", "covered", "claims process"], "angry"),

        # Scenario 6: Claimant is unsure if their policy covers a recent incident (from FlexInsurance PDS)
        ("Claimant is unsure if their policy covers a recent incident.",
         "I'm not sure if my policy covers theft from my balcony. Can you clarify?",
         "Of course, I can help with that. Let's check your policy wording together. Typically, theft from balconies is covered if the items were secured and there are signs of forced entry. Did you have any security measures in place?",
         ["theft", "balcony", "covered", "security measures"], "confused"),

        # Scenario 7: Claimant's beloved pet was injured (from any PDS, general scenario)
        ("Claimant's beloved pet was injured in an accident at the property.",
         "I'm heartbroken. My cat was injured when the ceiling collapsed. I had to rush her to the vet, and the bills are piling up.",
         "I'm so sorry to hear about your cat. That must be incredibly difficult for you. While we can't cover veterinary expenses directly, let's see if there's any other way we can assist you during this challenging time. Perhaps we can help with temporary accommodation costs or provide information on any available pet assistance programs.",
         ["sorry", "cat", "injured", "assist", "difficult time"], "sad"),

        # Scenario 8: Claimant is overwhelmed by the claims process (from any PDS, general scenario)
        ("Claimant is overwhelmed by the claims process and needs guidance.",
         "I'm so lost. I've never filed a claim before, and I don't even know where to begin.",
         "I understand it can feel overwhelming, especially if it's your first time. Don't worry, I'm here to guide you through every step of the way. Let's start by gathering some basic information about the incident, and then we'll discuss the next steps. I'll be with you every step of the way.",
         ["overwhelmed", "guide", "process", "information", "steps"], "anxious")
    ]

    return random.choice(scenarios)

# I am now ready to provide the second part of the code. Please let me know when you're ready to receive it.
def evaluate_response(user_response, ideal_response, customer_emotion, keywords):
  """Evaluates the user's response and provides constructive feedback."""

  analyzer = SentimentIntensityAnalyzer()
  user_sentiment = analyzer.polarity_scores(user_response)

  # Keyword matching
  user_words = set(user_response.lower().split()) - stop_words
  ideal_words = set(ideal_response.lower().split()) - stop_words
  keyword_match = len(user_words & set(keywords)) / len(ideal_words)

  # Sentiment analysis
  sentiment_score = 0
  if customer_emotion == "angry":
      target_sentiment = 0  # Neutral
  elif customer_emotion == "sad":
      target_sentiment = 0.3  # Slightly positive
  else:  # confused or anxious
      target_sentiment = 0  # Neutral

  sentiment_diff = abs(user_sentiment['compound'] - target_sentiment)
  sentiment_score = 30 * (1 - sentiment_diff)

  # Additional NLP checks
  empathy_keywords = ["understand", "sorry", "empathize", "feel", "concern"]
  clarity_keywords = ["explain", "clarify", "details", "process", "steps"]
  reassurance_keywords = ["assure", "help", "support", "걱정하지 마세요", "安心してください"]

  additional_score = 0
  if customer_emotion == "sad" and any(keyword in user_response.lower() for keyword in empathy_keywords):
      additional_score += 10  # Reduced weight for additional checks

  if (customer_emotion == "confused" or customer_emotion == "anxious") and any(keyword in user_response.lower() for keyword in clarity_keywords + reassurance_keywords):
      additional_score += 10

  # Overall score
  score = 40 * keyword_match + sentiment_score + additional_score

  # Feedback (more nuanced based on score)
  if score >= 80:
      feedback = "Excellent! Your response effectively addressed the customer's concerns and emotional state."
  elif score >= 60:
      feedback = "Good job! Your response shows empathy and provides some helpful information. Consider further refining it by including more specific details or next steps."
  elif score >= 40:
      feedback = f"Your response is on the right track, but it could be improved. Try to incorporate these key points:\n- {ideal_response}"
  else:
      feedback = f"This response might not be the most effective. A better approach would be:\n- {ideal_response}\nFocus on acknowledging the customer's {customer_emotion} and offering clear guidance."

  return score, feedback

def main():
    print("Welcome to the CHU Underwriting Dispute Call Simulator!")
    print("You will be presented with a dispute scenario and a simulated customer dialogue.")
    print("Respond as you would in a real call, adapting your tone and language accordingly.")

    while True:
        scenario, customer_dialogue, ideal_response, keywords, customer_emotion = get_random_dispute_scenario()
        print("\nScenario:", scenario)
        print("Customer:", customer_dialogue)
        user_response = input("Your response: ")

        score, feedback = evaluate_response(user_response, ideal_response, customer_emotion, keywords)
        print(f"\nEvaluation: {score:.2f}%")
        print(feedback)

        if input("\nAnother scenario? (y/n): ").lower() != 'y':
            break

    print("\nThank you for using the simulator!")

if __name__ == "__main__":
    main()
