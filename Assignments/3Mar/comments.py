from flask import Flask, render_template

app = Flask(__name__)

# Given data format
comments = [
    {
        "username": "John",
        "comment": "This product is good",
        "likes": 120,
        "flagged": False
    },
    {
        "username": "Amit",
        "comment": "This service is dumb and stupid",
        "likes": 45,
        "flagged": True
    },
    {
        "username": "Priya",
        "comment": "Excellent experience. Highly recommended!" * 10,
        "likes": 200,
        "flagged": False
    },
    {
        "username": "Sara",
        "comment": "Not satisfied",
        "likes": 15,
        "flagged": False
    }
]

@app.route("/comments")
def show_comments():

    inappropriate_words = ["dumb", "stupid"]

    # Clean & process comments
    for c in comments:
        c["comment"] = c["comment"].strip()

        for word in inappropriate_words:
            c["comment"] = c["comment"].replace(word, "****")

    total_comments = len(comments)
    total_flagged = len([c for c in comments if c["flagged"]])
    most_liked = max(comments, key=lambda x: x["likes"])
    all_usernames = ", ".join([c["username"].upper() for c in comments])

    return render_template(
        "comments.html",
        comments=comments,
        total_comments=total_comments,
        total_flagged=total_flagged,
        most_liked=most_liked,
        all_usernames=all_usernames
    )

if __name__ == "__main__":
    app.run(debug=True)