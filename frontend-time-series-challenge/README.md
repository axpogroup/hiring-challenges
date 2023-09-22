# Frontend Data Visualisation Challenge

Welcome to the Frontend Challenge! 

We hope you will enjoy the task and be able to show off some of your skills :)

Please invest **no more than 8 hours**, If you cannot complete the task in this time frame, document where you got stuck, so we can use this as a basis for discussion for your next interview.

Happy coding :)

## Task

As a User i want to visualise data and be able to identify outliers.

### Features

- Page Title
    - tell the user what the page is about
- Generate data
    - Include a button that generates data
        - for the last 100 days
        - with values >= 0 and <= 100, integer values only
    - consecutive click removes old data and creates a new one, but does not reset threshold value
    - data is not generated when user enters the page
- Threshold
    - include an input that takes value from >= 0 to <= 100, integer values only
    - defaults to 0
    - include an apply button, to apply changes
- Chart
    - displays data as a line chart
    - if no data, display an appropriate message 
    - displays threshold as a horizontal line if the threshold value is > 0
- Outliers
    - an Outlier is a value above the threshold
    - include a table with the following columns:
        - date in format: DD-MM-YYYY
        - value
        - error: value - threshold, i.e. 50 - 20 = 30
    - the table should only include outliers
    - if no outliers, then include a positive message
- (optional)
    - if you have time and you want, you can include any other feature that is not listed above and present it during the interview

### Requirements

- use React and Create-React-App,
- TypeScript
- for styling only Styled-Components, you have to create components yourself
- Chart library of your choosing
- use Git and commit your changes as you do
- you cannot use any library to handle Date, like MomentJS, etc.
- do not write any test, and remove the ones that come with CRA
- make sure your code is properly formatted / linted and doesn’t have any unused files / errors
- make the page look good and be clear for the user on desktop screen size, no need for full responsiveness
- colors, sizes, text messages are up to you

## Next steps

Once you finish the task, please upload the code to your Github repository and share us the link.

If you have any questions about the task, feel free to contact us.

During the next interview we will ask you to present the solution and tell us about challenges / shortcuts that you had to take.
