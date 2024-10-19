# Irish craft house

![AmIResponsive image of Irish Craft House](docs/amiresponsive.PNG)
[![](docs/images/devices-mockup.png)](https://irish-craft-house-shop.herokuapp.com/)
[Link to Live Site](https://irishdesignhousepp5-45c81a68233a.herokuapp.com/)

## Table of Contents

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## Introduction

The project is an e-commerce website for a shop that offers designer craft items made in Ireland.

Both guests and registered users can explore products and add items to their shopping cart.

Registered users have the ability to place orders, create a wishlist, save their details for future visits, and view their past orders.

## User Experience

### User Goals

The main user goal would be to allow users to browse items easily on the site. The user should be able to view details of chosen items before deciding to buy. They should be able to add or remove items to their shopping basket and change the amount they would like. Users should be able to view and edit details about their account when logged in and change details.

### Site Owner Goals

The site owners main goal would be to be able to have full CRUD (Create, Read, Update, and Delete) functionality for products on the site. They should also be able to edit other content via the admin panel and to communicate with customers via email.

### User Stories

Seven Epics were decided upon with a total of 30 user stories. All user stories can be viewed here [Projects board](https://github.com/users/astro-mat/projects/4/views/1). Each user story was categorized into one of the following classes: Must have, Should have, Could have, or Won't have. Points were given to each user story based on the estimated time required for completion.

| Class | Points | Percentage of total points |
| -------------- | --------- | --------------- |
| Must have | 65 p | 54 % |
| Should have | 51 p | 43 % |
| Could have | 0 p | 0 % |
| Won't have | 4 p | 3 % |

The following user stories were completed in the first release of the Irish craft house website. To view the Won't have, they are listed here [Projects board](https://github.com/users/astro-mat/projects/4/views/1).

#### Epic 1: Viewing and navigation
**User Story - View a list of products**

As a shopper, I can view a list of products so that I can select some to purchase						

Acceptance Criteria 1 - When I navigate to the main product page, I see a grid or list of products.

**User Story - View a specific category of products**

As a shopper, I can view a specific category of products so that I can quickly find products I'm interested in without having to search though all products.						

Acceptance Criteria 1 - Users can find and select from a list of available product categories.

Acceptance Criteria 2 - Only products belonging to the selected category appear in the results.

Acceptance Criteria 3 - The display accurately reflects the category's contents.

**User Story - I can View individual product details**

As a Shopper, I can View individual product details so that I can identify the price, description, product rating, product image and available sizes.

Acceptance Criteria 1 - The product page shows all relevant details such as name, description, price

Acceptance Criteria 2 - High-quality images of the product are presented.

Acceptance Criteria 3 - "Add to Cart" and "Buy Now" buttons are prominently displayed.

**User Story - Quickly identify deals, clearance items and special offers**

As a Shopper, I can Quickly identify deals, clearance items and special offers so that I can take advantage of special savings on products I'd like to purchase.

Acceptance Criteria 1 - Prominent visual indicators for deals and discounts

Acceptance Criteria 2 - Easy-to-access deal listings

Acceptance Criteria 3 - Clear product information about promotions

**User Story - Easily view the total of my purchases at any time**

As a Shopper, Easily view the total of my purchases at any time so that I can avoid spending too much.

Acceptance Criteria 1 - The total is displayed prominently and updates in real-time as purchases are made.

Acceptance Criteria 2 - Shopper	find out information about the organisation	Decide if I like this company and what they stand for

Acceptance Criteria 3 - An "About Us" or similar section is prominently linked in the footer or header of every page.

**User Story - find answers to questions I may have**

As a Shopper, find answers to questions I may have so that I can be more informed before I decide to purchase.

Acceptance Criteria 1 - A dedicated FAQ page is easily accessible from the main navigation menu.

#### Epic 2: Registration and user accounts	

**User Story - Easily register for an account**

As a Site User, easily register for an account so that I can have a personal account and be able to view my profile.

Acceptance Criteria 1 - The registration form is concise and requires minimal information.

Acceptance Criteria 2 - The registration form submits promptly without unnecessary delays.

Acceptance Criteria 3 - After successful registration, users are shown a confirmation message.
							
**User Story - Easily login or logout**

As a Site User, easily login or logout so that I can access my personal account information.

Acceptance Criteria 1 - The login form is easily accessible and prominently displayed.

Acceptance Criteria 2 - Users receive immediate confirmation of successful login or logout.

Acceptance Criteria 3 - The interface clearly indicates whether the user is logged in or logged out.

**User Story - Easily recover my password in case I forget it**

As a Site User, easily recover my password in case I forget it so that I can recover access to my account.

Acceptance Criteria 1 - A clear "Forgot Password" link is visible on the login page.

Acceptance Criteria 2 - The system sends a password reset link to the registered email address.

Acceptance Criteria 3 - Upon successful password reset, users are notified and redirected to the login page.

**User Story - receive an Email confirmation after registering**

As a Site User, receive an Email confirmation after registering so that I can verify that my account registration was successful.

Acceptance Criteria 1 - An email is automatically sent to the registered email address immediately after registration.

Acceptance Criteria 2 - The subject line clearly indicates it's a confirmation email.

Acceptance Criteria 3 - The email is sent promptly after successful registration.

**User Story - have a personalised user profile**

As a Site User, have a personalised user profile so that I can view my personal order history and order confirmation and save my payment information..

Acceptance Criteria 1 - Users can quickly access their profile from a dedicated menu item.

Acceptance Criteria 2 - Users can edit and update their personal details through the profile page.

Acceptance Criteria 3 - Users can manage their account settings, notification preferences, and privacy options.

**User Story - Can access Emails sent via the website**

As an admin, I Can access Emails sent via the website so that I can see what emails have been sent via the website.

Acceptance Criteria 1 - Administrators have a dedicated section to view all emails sent through the website.

Acceptance Criteria 2 - Email logs include sender, recipient, subject, and timestamp.
							                                
**User Story - **

As a Shopper, contact the website admin so that I can ask any questions that I need to ask.

Acceptance Criteria 1 - A prominent "Contact" link or button is visible on the website.

Acceptance Criteria 2 - The contact form is simple and easy to fill out.

Acceptance Criteria 3 - Users receive immediate confirmation of form submission.		
                                    
                                    
**User Story - **

As a Shopper, I can add items to a wish list so that I can Decide weather or not to buy it later.

Acceptance Criteria 1 - A dedicated "Add to Wish List" button is visible on product pages.

Acceptance Criteria 2 - Items are immediately added to the user's wish list when clicked.

Acceptance Criteria 3 - Users can easily access and view their wish list from a dedicated page.	
                                    
#### Epic 3: Sorting and searching	    

**User Story - sort the list of available products**

As a Shopper, sort the list of available products so that I can easily identify the best rated, best priced and categorically sorted products.

Acceptance Criteria 1 - Users can sort products by at least three criteria: best-rated and category.

Acceptance Criteria 2 - Sorting options are clearly visible and easily selectable.

Acceptance Criteria 3 - The sorted list updates immediately when a new sorting option is chosen.
                                    
**User Story - sort a specific category of product**
                                    
As a Shopper, I can sort a specific category of product so that I can find the best-priced or best-rated product in a specific category or sort the products in that category by name.

Acceptance Criteria 1 - Sorting directions (ascending/descending) are provided for each option.

Acceptance Criteria 2 - Users can easily see which sorting criterion is being applied at any given time.

                             
**User Story - sort multiple categories of products simultaneously**
                                    
As a Shopper, I can sort multiple categories of products simultaneously so that I can find the best-priced or best-rated products across broad categories such as "homewares" or "Jewellery".

Acceptance Criteria 1 - Users can select multiple categories to sort together.

Acceptance Criteria 2 - The sorting algorithm applies the chosen criteria uniformly across all selected categories.

Acceptance Criteria 3 - Users can easily see the combined result of their selections.					
                                    
**User Story - I can search by a product name or description**
                                    
As a Shopper, I can search by a product name or description so that I can find a specific product I'd like to purchase.

Acceptance Criteria 1 - Users can search for products using both exact matches and partial matches of names and descriptions.

Acceptance Criteria 2 - A prominent search bar is easily accessible on product pages and the main site.


**User Story - **
                                    
As a Shopper, I can easily see what I've searched for and the number of results so that I can quickly see whether the product I want is available.

Acceptance Criteria 1 - The number of results found is prominently displayed near the search box.

Acceptance Criteria 2 - A list of search results is shown on the search results page.

#### Epic 4: Shopping cart management
                                    
**User Story - Add items to shopping cart**
                                    
As a Shopper, I can Add items to shopping cart so that I can Purchase the items at the same time.

Acceptance Criteria 1 - Clicking the "Add to Cart" button adds the item to the cart.

Acceptance Criteria 2 - The cart icon displays the number of items in the cart.

Acceptance Criteria 3 - The cart total updates automatically after adding items
    							
                                    
**User Story - Remove items from shopping cart**
                                    
As a Shopper, I can Remove items from shopping cart so that I can reduce the selection of items that I want to buy.

Acceptance Criteria 1 - Clicking the "Remove" button removes the item from the cart.

Acceptance Criteria 2 - The cart icon updates to reflect the new item count.

Acceptance Criteria 3 - The cart total adjusts accordingly after removing items.
                                    
        							
**User Story - Change quantity in shopping cart**
                                    
As a shopper, I can Change quantity in shopping cart so that I can change how many of individual items I wish to purchase.

Acceptance Criteria 1 - Entering a value in the quantity field updates the cart total.

Acceptance Criteria 2 - Clicking "Update" applies the quantity change.

Acceptance Criteria 3 - The cart displays the updated quantity and price.

#### Epic 5: Account management	                            
                                    
**User Story - View account details**
                                    
As a Logged in user, I can View account details so that I can check if they are correct.

Acceptance Criteria 1 - My profile information is displayed on the account page.

Acceptance Criteria 2 - All order history is visible.

Acceptance Criteria 3 - My saved addresses and payment methods are accessible.


**User Story - Edit account details**
                                    
As a Logged in user, I can Edit account details so that I can make changes if they need to be made.

Acceptance Criteria 1 - I can update my name, email, and password

Acceptance Criteria 2 - Changes are reflected immediately upon saving

Acceptance Criteria 3 - Error messages are displayed for invalid inputs
    								
#### Epic 6: admin panel functionality
                     
**User Story - Create products**
                                    
As an admin, I can create products so that I can sell new products on the site.

Acceptance Criteria 1 - I can add product name, description, price, and images

Acceptance Criteria 2 - Categories and tags can be assigned to products

Acceptance Criteria 3 - Product creation is confirmed with a success message
    								
                                    
**User Story - Update product details**
                                    
As an admin, I can update product details so that I can make changes to products when they change.

Acceptance Criteria 1 - I can modify product name, description, price, and images

Acceptance Criteria 2 - Category and tag assignments can be changed

Acceptance Criteria 3 - Updated product information is reflected immediately
        						
    					
**User Story - Remove products from the site**
                                    
As an admin, I can remove products from the site so that I can remove them when they become non-stock items.

Acceptance Criteria 1 - Deleting a product removes it from the catalog

Acceptance Criteria 2 - Associated orders are marked as canceled

Acceptance Criteria 3 - A confirmation message is displayed after deletion

#### Epic 7: email communication
								
**User Story - Send order confirmation emails**
                                    
As an admin , I can Send order confirmation emails so that I can confirm to the customer that an order has been received.

Acceptance Criteria 1 - Emails are sent automatically after successful checkout

Acceptance Criteria 2 - Order details are included in the email

Acceptance Criteria 3 - Recipients can easily access their order status
                                    
        						
**User Story - send automated password reset emails**
                                    
As an admin, I can send automated password reset emails so that I can allow users to use the logged in functions automatically in the event of password loss.

Acceptance Criteria 1 - Emails are sent automatically when a password reset request is made

Acceptance Criteria 2 - Reset link is valid for a limited time

Acceptance Criteria 3 - Password reset is confirmed via email after successful change

## Design

The website was designed with a clean, simple look to reflect the quality design aspect of the brand. Simple black and white colour scheme was chosen which supported this choice and provided high contrast.

### Typography

The typography was chosen to fit in with the design style established by the colour choices earlier while still being easy to read. Capitalisation was employed for titles to re-enforce this design choice.

### Imagery

High quality imagery was important as it signals to prospective customers what they can expect. Wherever possible, lifestyle images are used to re-enforce the brand

### Wireframes
Wireframes were made using [Balsamiq](https://balsamiq.com/) of the home page and products page. 

#### Home page
![](docs/images/wireframe-landing-page.png)

#### Products page
![](docs/images/wireframe-products.png)

<!--

## Features

### Header

#### Navigation bar

![Navigation bar as a not logged in user](doc/navbar-not-logged-in.PNG)

- The navigation bar makes it easy for the user to navigate the site. 
- The user can find the different parts of the home page (and will include more in future versions) and enables the user to login to the portal and log out.
- The navbar is fixed to the top of all pages to allow easy navigation

![Navigation bar as a logged in user](doc/navbar-logged-in.PNG)

Once the user is logged in, the navbar changes. "Register/Login" changes to "Logout"

### Index page

#### Hero image

![Hero image at index page](doc/hero-image.PNG)

- The hero image is a simple backdrop of the stone walls of the studio outlining the opening theme of the site. Over the top of this is a bold large transparent version of the studio logo in white.
- This section provides the user with a clear visual opening to the site and what to expect
- Below the logo is a call to action button inviting the user to "click to make booking"

#### About Us Section

![About us Section at index page](doc/about-us.PNG)

- Next up is a short section of text giving a brief description of the studio and its origins.

#### Gallery Section

![Gallery at index page](doc/gallery.PNG)

### Booking Info Page

![Booking Info page](doc/booking-info.PNG)

- The site user is brought to a page after clicking the hero image call to action button that details the studio opening hours
- The user is then invited to click another to log in to the Client portal in order to see studio availability and make a booking.

### Sign In Page

![Sign in page with fields for email and password](doc/sign-in.PNG)

The sign-in page allows existing users to log in, enhancing the user experience by eliminating the need to enter their email each time they want to make a booking. It also enables users to view all their bookings in one place.

### Register Page

![Register page with fields for email, username, password and password again](doc/register.PNG)

The Register page includes fields for the user to enter their email, username, password, and password confirmation. This ensures the user registers a contact method and avoids typos in the password.

### Booking Detail Page

![Booking detail page](doc/booking-detail.PNG)

- This is the main page that the user is brought to after logging in
- At the top of the page, the user is invited to make a new booking. There is text inputs for Artist name, date of booking and booking requirements.
- The date opens a date box. The user is unable to enter a date that is in the past or is booked by any other artist.
- A button allows the user to make their booking.
- Below this area is a list of bookings already made by this user.
- Within this area, there are buttons to edit or delete each booking

### Booking Successful Page

![Booking Success page](doc/booking-success.PNG)

- After the user has made a booking, they are brought to this page.
- A simple summary of their booking is displayed
- A button allows the user to be directed back to the booking detail page.

### Edit Booking page

![Edit Booking page](doc/edit-booking.PNG)

- Once a user decides to edit a booking from the booking detail page, they are brought here.
- The current details of the booking are displayed in text boxes. 
- The user can edit any of the booking details.
- The user can then use the buttons to either save the changes or cancel editing.
- They are then brought back to the booking detail page and an alert informs them of their change.

### Booking delete page

![Edit Booking page](doc/booking-delete.PNG)

- When a user clicks on "Delete" button on booking detail page, they are bought to this page.
- The booking details are displayed and the user is asked if they are sure they want to delete or cancel the deleting process.
- If they decide to delete, they are bought back to the booking detail page with confirmation that the booking was deleted and the table has updated.
- If they change their mind and cancel, they are also brought back to the booking detail page with no changes having been made.

### Log Out Page

![Log Out page](doc/logout.PNG)

- Once the user is finished, they can click the Logout button
- They are then taken to the Log out page where they are asked to confirm that they want to log out
- They can then choose to continue and be redirected to the index page.
- Otherwise, they can click "Back to my bookings" or go anywhere using the navbar menu

### Footer

![footer](doc/footer.PNG)

- The footer section includes links to Studio Moo Moo's Facebook, Instagram and twitter pages.
- The design colour and styling reflect those of the header
- The links open to a new tab to allow easy navigation for the user. 
- The footer is valuable to the user as it allows them to find and follow on social media.
- There is also a small piece of stating the copyright restriction

### Password Reset Page

![password Reset Page](doc/password-reset.PNG)

- In the event of a user forgetting their password and being unable to login, on the login page, there is a link labeled "forgot password?"
- On clicking this link, they are brought to this page.
- Here they are prompted to enter their email. once submitted, an email is sent with instructions on how to change password.

![Password reset email sent](doc/password-reset-sent.PNG)

- Once the request to reset has been submitted, the user is taken to this page and they are instructed to follow the institutions on the email when they receive it.

### Alerts

![Alert](doc/alert.PNG)

- When major changes are made by the user, a high contrast alert is visible just below the header
-->






<!-- 
## Features to be Added

Several features can be added in the future.

- Add more content to home page.
- add "contact me" section.
- Date order for bookings on booking detail page.
- Sign in with Social media account or Google credentials.
- Captcha verification when the user is signing up with email address.
- Guidance when a user sign in for the first time.
- Add more functionality to the portal. The proposed media sharing and editing function

## Testing

### Validation of Code

#### HTML

![Screenshot of HTML validation of index page](doc/index-html-valid.PNG)

All the pages were tested at the [W3C Markup Validation Service](https://validator.w3.org/). The index page validation is above, all the other validations are linked below.

- [Sign In Page](doc/sign-in-html-valid.PNG)
- [Login Page](doc/register-html-valid.PNG)
- This page showed 4 errors. These seem to originated from AllAuth injected html and as such are not available for me to edit
- [Booking Detail Page](doc/booking-detail-html-valid.PNG)
- [Booking Successful Page](doc/booking-successful-html-valid.PNG)
- [Edit Booking page](doc/edit-booking-html-valid.PNG)
- [Booking delete page](doc/booking-delete-html-valid.PNG)
- [Log Out Page](doc/log-out-html-valid.PNG)
- [Password Reset Page](doc/password-reset-html-valid.PNG)

#### CSS

![Screenshot of CSS validation](doc/css-valid.PNG)

The CSS code was tested at [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). The process completed without errors but generated one warning: "Imported style sheets are not checked in direct input and file upload modes." This warning pertains to fonts imported from Google Fonts.

#### Python

All Python files have been validated using the [CI Python Linter](https://pep8ci.herokuapp.com/) to ensure they meet PEP8 standards. The validation process completed without any errors.

**Booking - views.py**

![Python validation of views.py in bookings](doc/pep8-booking-views.PNG)

**Booking - models.py**

![Python validation of models.py in booking](doc/pep8-booking-models.PNG)

**Booking - admin.py**

![Python validation of admin.py in booking](doc/pep8-booking-admin.PNG)

**Booking - forms.py**

![Python validation of forms.py in booking](doc/pep8-booking-forms.PNG)

**Booking - urls.py**

![Python validation of urls.py in booking](doc/pep8-booking-urls.PNG)

**Booking - apps.py**

![Python validation of apps.py in booking](doc/pep8-booking-apps.PNG)

### Lighthouse

Tests in Lighthouse were performed for both desktop and mobile.

#### Desktop

![Lighthouse test for desktop](doc/lighthouse-desktop.PNG)

The test for desktop resulted in scores all over 90.

#### Mobile

![Lighthouse test for mobile](doc/lighthouse-mobile.PNG)

The test for mobile resulted in scores all over 90. The performance rating could be further improved by adopting responsive images in order to reduce mobile load time.

### Wave Webaim - accessibility testing

The accessibility test at [Wave Webaim](https://wave.webaim.org/) resulted without errors and contrast errors on all pages.

#### Index page

![Wave webaim test of index page](doc/wave-webaim.PNG)

#### Sign In

![Wave webaim test of Sign In page](doc/wave-webaim-sign-in.PNG)

#### Register page

![Wave webaim test of Login page](doc/wave-webaim-Register.PNG)

#### Booking Detail page

![Wave webaim test of Booking Detail page](doc/wave-webaim-booking-detail.PNG)

#### Booking Successful page

![Wave webaim test of Booking Successful page](doc/wave-webaim-booking-successful.PNG)

#### Edit Booking page

This page would not load with webAID. See Bugs section

#### Booking delete page

![Wave webaim test of Booking delete page](doc/wave-webaim-booking-delete.PNG)

#### Log Out page

This page would not load with webAID. See Bugs section

#### Password Reset page

![Wave webaim test of Password Reset page](doc/wave-webaim-password-reset.PNG)

### Contrast Grid

The [Contrast Grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23CACACA%2C%20%20Background%20color%0D%0A%23353535%2C%20Text%0D%0A%23411919%2C%20Cancel%20btn%20-%20background%0D%0A%23FFFFFF%2C%20Cancel%2Fconfirm%2Fdelete%20btn%20-%20text%0D%0A%23193A18%2C%20Confirm%20btn%20-%20background%0D%0A%238d3838%2C%20Delete%20btn%20-%20background%0D%0A%23000000%2C%20Footer%20icons&es-color-form__tile-size=compact&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp) resulted in only AAA results for the combination used on the webpage. The main combination throughout the page is #000000 and #FFFFFF which has a value of 7+ which is the best result available.

![Contrast Grid of the webpage](doc/contrast-grid.PNG)
-->

### Search Engine Optimization (SEO) & Social Media Marketing

#### Keywords

To enhance Google search index ratings, various tools were utilised, including Moz and QuestionDB, to identify relevant keywords for incorporation into meta tags, alt-text descriptions, and content elements of the project.

The first step was to brainstorm general topics and keywords; 
###### General Handmade Craft Items
- Handmade crafts
- Unique handmade items
- Artisan goods
•	Handcrafted products
•	Irish handmade crafts
•	Celtic crafts
•	Traditional Irish crafts
###### Specific Categories
- Handmade jewellery
- Knitted items
- Woodcarvings
- Pottery
- Textiles
- Glasswork
- Metalwork
- Leathercraft
- Ceramics
- Embroidery
###### Seasonal/Holiday-Themed Crafts
- Christmas ornaments
- Easter decorations
- Halloween accessories
- St. Patrick's Day gifts
- Valentine's Day crafts
- Summer garden decor
- Autumn-themed crafts
###### Irish-Themed Crafts
- Shamrock designs
- Celtic knot patterns
- Leprechaun figurines
- Claddagh rings
- Irish heritage crafts
- Celtic cross jewelry
- Triskelion symbols
###### Long-Tail Keywords
- Handmade Irish wool scarves
- Customizable Celtic-inspired jewelry
- Hand-painted Irish pottery
- Hand-knitted Aran sweaters
- Handmade Irish crystal jewelry
- Hand-carved wooden Irish flutes
- Handmade Irish linen table runners

These were then assessed for relevance and authoritativeness.

##### Relevance Assessment
- General keywords: Highly relevant
    Terms like "handmade crafts," "artisan goods," and "unique handmade items" directly relate to the website's offerings.
- Specific categories: Moderately relevant
    While specific categories like "knitted items" or "woodcarings" are relevant, they might be too broad for SEO purposes.
- Seasonal/holiday-themed crafts: Relevant but limited
    These keywords are seasonal and may have limited long-term impact.
- Irish-themed crafts: Very relevant
    Keywords like "Celtic crafts" and "Irish heritage crafts" are highly relevant to the target audience.
- Long-tail keywords: Most relevant
    These specific product descriptions are highly targeted and likely to attract relevant traffic.
##### Authoritativeness Assessment
- General terms: Good foundation
    Using authoritative terms like "handmade crafts" establishes credibility.
- Specific categories: Limited authority
    While specific categories exist, they don't necessarily convey expertise.
- Irish-specific terms: Strong authority
    Terms like "Irish heritage crafts" suggest deep knowledge of Irish craft traditions.
- Long-tail keywords: Strong authority
    These specific product descriptions demonstrate expertise in particular craft types.

Based on this, the top keywords could be identified:

- Handmade Irish crafts
- Unique Celtic-inspired jewellery
- Traditional Irish pottery
- Hand-knitted Aran sweaters
- Customizable Irish crystal jewellery
- Hand-carved wooden Irish flutes
- Handmade Irish linen table runners
- Shamrock designs
- Claddagh rings
- Irish heritage crafts


#### Metadata
based on this research base.html and index.html were changed in order to better represent the identified keywords. The main logo was changed from a H1 tag to a span so that our H1 could be used in the hero image with two of our identified keywords.

![Span version of header logo](docs/SEO-header-logo.PNG)

#### Sitemap

#### Robots

#### Social Media Marketing

#### Newsletter Marketing


<!-- 
### Manual Testing

Every page at the website has been manually tested. It is done in Google Chrome DevTools and on different devices. The devices used were one mobile phone, one laptop and one external screen:

- Samsung Galaxy A52s (1080 x 2400)
- HP 250 G4 Notebook PC (1366 x 768)
- HP 2309v LCD Screen (1920 x 1080)

#### Navigation bar

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Home link | When clicked, directs the user to the home page | Click at "Home" | Got directed to the home page | Pass |
| Logo link | When clicked, directs the user to the home page | Click at "Logo" | Got directed to the home page | Pass |
| About link | When clicked, directs the user to the about section of the Home page | Click at "About" | Got directed to the about section of the Home page | Pass |
| Gallery link | When clicked, directs the user to the Gallery section of the home page | Click at "Gallery" | Got directed to the Gallery section of the home page | Pass |
| Register/Log in link | When clicked, directs the user to the Log in page | Click at "Register/Log in" | Got directed to the Log in page | Pass |
| Bookings link not visible (signed out) | Bookings link not visible as a signed out user | Sign out and inspect navigation bar | Bookings link not visible | Pass |
| Bookings link visible (signed in user) | Bookings link visible as a signed in user | Sign in, check navigation bar | Bookings link visible | Pass |
| Bookings link | When clicked, directs the signed in user to the Bookings page | Sign in, click at "Bookings" | Got directed to the Bookings page | Pass |
| Log Out link not visible (signed out) | Log Out link not visible as a signed out user | Log Out and inspect navigation bar | Log Out link not visible | Pass |
| Log Out link visible (signed in user) | When clicked, directs the user to the Log Out page | Click at "Log Out" | Got directed to the Log Out page | Pass |
| Log Out link | When clicked, directs the signed in user to the Log Out page | Sign in as a staff or superuser, click at "Log Out" | Got directed to the Log Out page | Pass |

#### Index page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The index page was responsive and changed depending on screen size | Pass |
| "Click to make booking" button | Directs the user to the Register/Login page | Click at the "Click to make booking" button | Got directed to the Register/Login page | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |

#### Log In Page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| All fields required | An error message appears when the user tries to sign in but leaves one field empty | Leave one field empty one by one and try to Sign In | An error message appeared when a field was left empty | Pass |
| Remember me button | when selected when logging in, user details are remembered at next login | select when logging in, log out and return | User details were remembered on returning to the page | Pass |
| Sign In button | When the "Sign In" button is pressed, the user gets signed in | Click at "Sign In" button | The user gets signed in | Pass |
| Redirected | When the "Sign In" button is pressed, the user gets redirected to the booking detail page | Visit Register page, click Sign in, press "Sign In" button | The user got redirected to Booking Detail page | Pass |
| Sign Up button | When the "Sign Up" button is pressed, the user redirected to Register page | Click at "Sign Up" button | The user gets redirected to Register/Login page | Pass |
| Forgotten Password Link | When link is clicked, user is redirected to password reset page | Visit Log In page, click on "Forgot password" Link | When link is clicked, user is redirected to password reset page | Pass

### Register page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| All fields required | An error message appears when the user tries to sign up but leaves one field empty | Leave one field empty one by one and try to Sign Up | An error message appeared when a field was left empty | Pass |
| Redirected | When the "Sign Up" button is pressed, the user gets redirected to the Booking Detail Page  | Visit Register page, fill out all required fields, press "Sign Up" button | The user got redirected to Booking Detail page | Pass |

#### Booking Detail page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| All fields required | An error message appears when the user tries to make a booking but leaves one field empty | Leave one field empty one by one and try to Make a booking | An error message appeared when a field was left empty | Pass |
| Redirected after "Make A Booking" | When the "Make a booking" button is pressed, the user gets redirected to the Booking Success Page  | Visit Booking Detail page, fill out all required fields, press "Make a booking" button | The user got redirected to Booking Success page | Pass |
Edit Booking Redirect| When the "Edit" button is pressed, User is redirected to Edit Booking page | Visit Booking Detail Page, Select a booking to edit, Click "Edit" | The user got redirected to Edit Booking page for that booking | Pass |
Delete Booking |  When the "Delete" button is pressed, User is redirected to Edit Delete Booking page | Visit Booking Detail Page, Select a booking to delete, Click "Delete" | The user got redirected to Delete Booking page for that booking | Pass |
Date Validation | If the user attempts to make a booking on a date that there is already a booking booked, An error message appears and user is unable to proceed with that date | Visit Booking Detail Page, Fill in all fields, Select a date that is already booked, Click "Make A Booking" |  An error message appears when the user tries to click "Make A Booking if that date is unavailable | Pass

#### Booking Successful page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| Correct Information displayed | The page should display the details of the booking that the user just made | Visit "Booking Detail" page, click "Make A booking" | Booking Successful Page displays the information of the booking just made | Pass
| "Back to bookings" Button | When the "Back to Bookings" button is pressed, the user gets redirected to "Booking Detail" page | Click at "Back to bookings" button | The user gets redirected to "Booking Detail" page | Pass |

#### Edit Booking page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| Correct Information displayed | The page should display the details of the booking that the user just made | Visit "Booking Detail" page, click "Edit" |  Edit Booking Page displays the information of the booking to be edited | Pass
| Edit Booking | Any field can be edited | Visit Booking detail Page, select a booking to edit, click "Edit booking", Make changes to every field | All Fields are able to be edited | Pass
| "Save Booking" Button | After making a change, Clicking on "Save booking" button redirects user to Booking detail page and changes are displayed | Visit Edit Booking page, make a change to booking, click "Save Booking" | User is redirected to Booking detail page and changes are displayed | Pass

#### Booking delete page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| Correct Information displayed | The page should display the details of the booking that the user wants to delete | Visit "Booking Detail" page, click "Delete" |  Delete Booking Page displays the information of the booking to be Deleted | Pass
| "Delete Booking" Button | User is redirected back to Booking detail page, desired booking has been deleted | From delete booking page, click "Delete" | User is redirected back to Booking Detail page and the booking has been deleted | Pass 
| "Cancel" Button | User is redirected back to Booking detail page, desired booking has not been deleted | From delete booking page, click "Cancel" | User is redirected back to Booking Detail page and the booking has not been deleted | Pass 

#### Log Out page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| "Sign Out" Button | User is redirected to index page, Navbar menu has changed, user no longer has access to Bookings detail page | From Log out page, click "Sign out" button | User is redirected to index page, Navbar menu has changed, user no longer has access to Bookings detail page | Pass 
| "Back to my Bookings" | User is redirected back to Booking Detail page, Navbar menu has not changed, user still has access to Bookings detail page | From Log out page, click "Back to my Bookings" button | User is redirected to Booking Detail page, Navbar menu has not changed, user still has access to Bookings detail page | Pass 


#### Password Reset page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| All fields required | An error message appears when the user tries to reset password with field empty | Leave password field empty try to reset password | An error message appeared when a field was left empty | Pass |
| "Rest my Password" Button | 

#### Password reset done page

| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| Responsive design | The page changes so the content fit at the smallest to the largest screens without scrolling sideways | In DevTools, select the smallest device and make it larger step by step | The page was responsive and changed depending on screen size | Pass |
| Text readability | Enough margins and padding to make text readable | Read all text blocks at all different Bootstrap breakpoints | The text is readable at all breakpoints | Pass |
| Reset Email is sent and received | User receives an email with further instructions | Click on "Forgot Password" link from Log in page, enter email, click reset password, check if email is received | Email is received with instructions to reset | Pass

### Bugs

During the testing several bugs have been discovered.

When the html validation of all pages were completed, a number of errors were present but were all fixed.

Another validation error was when assessing for accessibility with webAID. two of the pages were unable to load in the tool and as such could not be assessed. However, since all the other pages flew through the tests, It can be assumed safely that these pages would pass as they are very similar in style

When the PEP8 validation of the Python code was made, 48 errors occurred. Most of them were one of following:
- trailing whitespace
- line too long
- blank line contains whitespace

The first lighthouse tests performed resulted in a 82 performance. This was improved by resizeng the images to its biggest dimension being 800px. Performance could be improved further by introducing responsive images

## Technologies Used

- [Code Institutes Gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template) - 
- [GitHub](https://github.com/)
- [Gitpod](https://www.gitpod.io/) 
- [Heroku](https://www.heroku.com/)
- [Balsamiq](https://balsamiq.com/)
- [Google Spreadsheet](https://docs.google.com/spreadsheets/)

The code languages used in this project are HTML, CSS, JavaScript and Python. The main frameworks used are Django and Bootstrap.

## Deployment

### Fork repository in GitHub

- Open the chosen repository in GitHub 
- Click on the "Fork" button
- A copy of the repository is now located in your own account

### Clone repository in GitHub

- Open the chosen repository in GitHub 
- Click on "Code" button
- Copy the URL
- Open your command line interface
- Navigate to the directory you want to clone the repository to
- Use 'git clone', followed by the earlier copied URL
- Move into the newly created directory
- Install the dependencies using 'pip install -r requirements.txt'
- Run the application with 'python manage.py runserver'

### Deployment to Heroku

- Open Heroku and log in
- Click on "New" and choose the option "Create new app"
- Choose an app name and which region (Europe or United States) you are located in
- Press "Create app"
- When the app is created, choose the Settings tab
- Under "Config Vars", press "Reveal Config Vars"
- In keys, write DATABASE_URL
- In value, insert the url to the database
- Press "Add"
- Under "Buildpacks", press "Add buildpack"
- Choose "Python", press "Add buildpack"
- Change tab to the Deploy tab
- Choose deploy method - GitHub
- Search for the correct repository name at your connected GitHub account
- Press "Connect"
- Under "Manual deploy", choose which branch to deploy and press "Deploy Branch"

Link to deployed website: <https://frisa-booking-e7f1e4a00ea9.herokuapp.com/>

## Credits

### Libraries Used

- django-allauth
- django-summernote
- gunicorn
- whitenoise

### Used resources

- [Font Awesome](https://fontawesome.com/) - For all icons on the website
- [W3Schools](https://www.w3schools.com/howto/howto_js_read_more.asp) - Used to troubleshoot/questions about code
- [django](https://docs.djangoproject.com/) - For all information referred to about Django

### Existing projects used for inspiration

- https://github.com/brodsa/findMEreadME
- https://github.com/LauraMayock/The-happy-reader
- https://github.com/KSDunne/statement_beauty/blob/main/makeover/forms.py
- https://github.com/FridaWikell/frisa-booking/blob/main/templates/index.html
- https://github.com/KSDunne/statement_beauty/blob/main/makeover/forms.py
- https://github.com/Thomas-Tomo/woodland-whispers-retreat/blob/main/cabin_bookings/models.py

### Tutorials and code snippets

- https://stackoverflow.com/questions/31574775/move-a-bootstrap-input-element-further-down-the-page - Code to move down element in bootstrap
- https://simpleisbetterthancomplex.com/tutorial/2019/01/03/how-to-use-date-picker-with-django.html
- https://mdbootstrap.com/docs/standard/navigation/footer/
- https://stackoverflow.com/questions/13881548/sticky-footer-hiding-content

## Acknowledgements

Many thanks to the following people for all their help and support

- Laura Mayock - Cohort Facilitator
- Antonio Rodriguez - Mentor
- Indre Vilickaite - Fellow Student
- Patrick Hladun - Fellow Student

And all the Tutors that assisted me

Holly, Roo, John, Roman, Sean, Oisin, Mark, Sarah, Thomas and Alan -->


 



<!-- 
TEMP TO BE DELETED-----------------------------------------------------------------------------------------------------------

CITATIONS

My project was heavily influenced by the excellent Code institute "Boutique Ado" walk through

Bootstrap mega menu -
https://welcm.uk/blog/mega-menu-with-bootstrap-4

Wish List Functionality:
https://stackoverflow.com/questions/56580696/how-to-implement-add-to-wishlist-for-a-product-in-django
https://github.com/jrief/django-shop-wishlists
https://django-oscar.readthedocs.io/en/2.1.0/_modules/oscar/apps/customer/wishlists/views.html
https://forum.djangoproject.com/t/creating-a-simple-add-to-cart-with-simple-functionalities/21992
https://djangopackages.org/grids/g/ecommerce/

FAQ Functionality:
https://docs.djangoproject.com/en/5.1/faq/help/
https://docs.djangoproject.com/en/5.1/ref/contrib/admin/
https://medium.com/django-unleashed/complete-django-project-setup-a-comprehensive-guide-289182b75f3c
https://stackoverflow.com/questions/54601455/add-menu-items-to-django-admin-site
https://www.w3schools.com/django/index.php

Contact Us section:
https://mailtrap.io/blog/django-contact-form/
https://stackoverflow.com/questions/67678948/how-to-add-a-functional-contact-form-at-my-home-page-in-django-by-using-inclu
https://www.twilio.com/en-us/blog/build-contact-form-python-django-twilio-sendgrid
https://www.youtube.com/watch?v=lSgRWA4PMt4
https://learndjango.com/tutorials/django-email-contact-form-tutorial
https://docs.djangoproject.com/en/5.1/ref/settings/
https://stackoverflow.com/questions/74417399/making-a-functional-contact-form-using-django
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms

PP5 project research
https://github.com/davidindub/coffeecrew
https://github.com/Zilvaro/adenwell-ecommerce
https://github.com/anthonyjn08/witness_the_fitness_v1
https://github.com/JoGorska/bonsai-shop
https://github.com/LewisMDillon/web-piano-academy


About Us Section:
Code institute "I Think therefore" I blog walk through
https://github.com/Code-Institute-Solutions/blog/tree/main/15_testing/about

Website research
https://leitrimdesignhouse.ie/




TO DO

- Go back to Shopping bag and apply fix that allows minus bag items in mobile view
- Check that nothing says "Boutique ado"
- mobile header matches full screen
- delete comments from all files
- Check that all images are there
- fix update amount in cart
- insert table of contents
- Delete all these notes at end of readme
- Mockup image at start of readme
- get rid of all comments in this readme


BUGS
- BASKET IS IN DOLLARS!!!!
- Double hamburger on mobile


FUTURE ADDITIONS
Special offers menu item


Concepts that will be required for your final project include:

SEO implementation, including:
A robots.txt file
A sitemap.xml file
Descriptive meta tags
rel attributes on links to external resources
Marketing techniques, including:
The need for the creation of either a real Facebook business page, or a mockup of one.
A newsletter signup form, either through a service such as MailChimp or through a custom implemented one.
The requirements for an e-commerce business model:
The necessity for the inclusion of an e-commerce business model, highlighting the purpose of the application as either B2B or B2C focused, and detailing the core business intents and marketing strategies for the application.


CHECKLIST
- At least 3 original custom models with associated functionalities, markedly different from those present in the Boutique Ado walkthrough project if they have been used as a basis for your project. (A note on custom models)
- At least one form on the front end, which provides either admin or regular users with CRUD functionality without having to access the admin panel.
- At least one UI element on the front end, which allows either admin or regular users to delete records in the database without having to access the admin panel.
- Evidence of agile methodologies followed during the development of your project in the GitHub repository.
- A robots.txt file.
- A sitemap.xml file.
- Descriptive meta tags in the HTML.
- At least one link to an external resource, which makes use of a rel attribute.
- A custom 404 error page.
- Evidence of either a real Facebook business page, or mock up of one, for the purposes of digital marketing.
- Evidence of a newsletter signup form for the purposes of digital marketing.
- A description of the e-commerce business model including marketing strategies in the README file.
- DEBUG mode set to False.
- Working functionality for users to register and log in and out of the application without issues.
- Working E-commerce functionality for users to make purchases within the application.
- Detailed testing write ups, beyond results of validation tools.
- GitHub project board set to public visibility. -->