# Heart Books

Welcome to 'Heart Books', this is a book rating website similar to Letterboxd where users can rate books they have read. This rating will be 0/5 stars, and books will have their rating's average displayed on their own page. User will also have a profile which will display their last read book.
Books will also have a comment sections for users to share their thoughts about that particular book.

## Table of Contents

1. [Project Purpose](#project-purpose)
2. [User Experience (UX)](#user-experience-ux)
	1. [Strategy](#strategy)
	2. [Scope](#scope)
	3. [Structure](#structure)
	4. [Skeleton](#skeleton)
	5. [Surface](#surface)
3. [Features](#features)
4. [Technologies Used](#technology-used)
5. [Testing](#testing)
6. [Credits](#credits)

## Project Purpose

The purpose of this project is to create a space where readers can have a recorded history of all the books they have read. I also wanted to create a kind of community, for me to be able to achieve this I implemented a comment section, and also rating. 
The rating shows what the census is on a book hopefully giving the an idea of what other people feel/think about the book. 
The profile pages bring a personal feel to the website allowing for recent reads to be displayed, and a small profile bio.
The library of books on the site will be built from user submissions. For example, a user will register, search for a book they have read, if this book is not on the site they can submit a book to be approved/rejected by an admin. This will then show in the search for other users who visit the site.

## User Experience (UX)

### Strategy

#### Site Goals

- Display categories such as recent read, popular books, etc. on home page
- User profile
- Books
- Book comment section
- Admin controls to approve/reject book submissions/comments

#### External User Goals

- Find something new to read based on different display section on the website
- Express their opinion on books they have read
- Rate different books

#### User Stories

#### Admin

1. As a **Site Admin** I can **create, read(view), update, and delete books** so that **I can manage my library of books**

AC1: Given a logged in user, they can create books
AC2: Given a logged in user, they can read(view) book(s) information
AC3: Given a logged in user, they can update books
AC4: Given a logged in user, they can delete books

2. As a **Site Admin** I can **approve or reject books, and comments** so that I can **manage objectional content**

AC1: Given a logged in user, they can approve content (books, comments)
AC2: Given a logged in user, they can reject content (books, comments)

#### Books

1. As a **User** I can **submit a book** so that **it can be approved to be rated**

AC1: Given a logged in user, they can submit a book for admin review.

2. As a **User** I can **click on a book** so that **I can view ratings, and comments**

AC1: When a book is clicked, a detailed view of the book is displayed.

3. As a **User** I can **submit a rating** so that **I can share a option based opinion**

AC1: Given a logged in user, when on a book page a rating option is available
AC2: When on a book page, a mean average, and collective rating is shown

#### Profile

#### About

1. As a **Site Admin** I can **edit the about page** so that **it can stay up-to-date with changes**

AC1: Give a logged in user, they can edit the text field

2. As a **Site Admin** I can **store contact submissions** so that I **view and analyse contact submissions**

### Scope

### Structure

The website will consist of the following pages, all using a base template to keep the page consistent for ease of navigation:

1. Home
2. Books
3. About
4. Profile

Each page will use a base template to keep the website consistent. The base template will be the navigation bar, and the footer of the website.

When visitors come to the website, and are not logged into an account they will see both options **'Login'** & **'Register'**. Once registered, and logged in the navigation bar will change to display **'Profile'** & **'Logout'**

#### Home

The home page will display the most recent book added to the books table. It will also have a short description of what the website is but not too much content.

Navigation bar at the top of page will be consistent on all pages allowing ease of navigation throughout the website.

#### Books

This will be a list of all the books that have been uploaded to the website, and that have been approved. This will paginated by 10, with a **'Next'** & **'Prev'** button at the bottom of the page.

#### About

#### Profile

### Skeleton

I have designed my website skeletons for the desktop, and mobile view via 'Lucid.app'. All designs can be found via the links in the table below:

| - | Home | Books | About | Profile |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| Desktop | [Link](/graphics/wireframe/heart_book_wireframe_desktop.pdf) | [Link](/graphics/wireframe/heart_book_wireframe_desktop.pdf) | [Link](/graphics/wireframe/heart_book_wireframe_desktop.pdf) | [Link]() |
| Mobile | [Link]() | [Link]() | [Link]() | [Link]() |
