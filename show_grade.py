"""Display your Homework 1 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "771bb144aa61e5476593ade442036911"
GRADE_HASH = "60d2a4b148d3123c6df65d931da5c8b1e791244ca2b01e06d9abc6fccc0651f7"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 1: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
