# Web Forms — Test Cases & Expected Behaviors

Source: QA Practice (https://www.qapractice.com) — free QA automation practice.

## TC01: Submit a fully valid form

Steps:
  1. Fill every field with valid values
  2. Select a communication preference
  3. Click Submit

Expected: Success message "Details Successfully Added!" is shown.

## TC02: Submit an empty form

Steps:
  1. Leave all fields empty
  2. Click Submit

Expected: A "required" error appears under each mandatory field.

## TC03: Invalid email format

Steps:
  1. Fill all fields correctly except email = "notanemail"
  2. Click Submit

Expected: Error "Invalid Email Address" is shown.

## TC04: Date of joining wrong format

Steps:
  1. Enter Date of Joining as 2021-06-01 (wrong format)
  2. Fill the rest validly
  3. Click Submit

Expected: Error "Date of Joining format should be dd/mm/yyyy" is shown.

## TC05: Missing communication preference

Steps:
  1. Fill all fields but select no radio
  2. Click Submit

Expected: Error "Please select a Communication Preference" is shown.

## TC06: Country dropdown options

Steps:
  1. Open the Country dropdown

Expected: Options include United States, Canada, United Kingdom, India, Australia, Other.

## TC07: Clear resets the form

Steps:
  1. Fill several fields
  2. Click Clear

Expected: All fields return to their empty/default state.

## TC08: Radio buttons are mutually exclusive

Steps:
  1. Select Email, then select Phone

Expected: Only Phone stays selected; the two radios are mutually exclusive.
