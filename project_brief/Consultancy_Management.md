### Consultancy Management App

A consultancy practice has approached you to build a web application to help them manage their clients and consultants. A consultant may look after many clients at a time. An client is registered with only one consultant.

#### MVP

- The practice wants to be able to register / track clients. Important information for the consultants to know is -
  - Name of client
  - Date Of Birth (use a VARCHAR initially) - \\ Date of engagement \\
  - Type of client
  - Contact details for the relationship manager
  - Treatment notes - \\ Services consultant hired \\
- Be able to assign clients to consultants
- CRUD actions for consultants / clients - remember the user - what would they want to see on each View? What Views should there be?

### Possible Extensions

- Mark relationship managers as being registered/unregistered with the consultant. unregistered relationship managers won't be able to add any more clients.
- If an relationship manager has multiple clients we don't want to keep updating contact details separately for each pet. Extend your application to reflect that an relationship manager can have many clients/ consultants and to more sensibly keep track of relationship managers' details (avoiding repetition / inconsistencies)
- Handle booking-in /booking-out dates
- Let the practice see all clients/ consultants currently in the practice (today's date is between the booking-in and booking-out?)
- Sometimes an relationship manager does not know the engagement date. Allow them to enter a month instead. Try and make sure this always up to date - ie if they visit again a year from now a 3 month engagement is now 4.
- Add extra functionality of your choosing - assigning servicess, a more comprehensive way of maintaining service notes over time. Appointments. Pricing / billing.
