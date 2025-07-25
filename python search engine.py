import webbrowser
website = input('search websites: ')

if website == 'google':
    google = input('search: ')
    webbrowser.open("https://www.google.com/search?q=" + google)
elif website == 'youtube':
   youtube = input('Search: ')
   webbrowser.open('https://www.youtube.com/results?search_query=' + youtube)
elif website == 'amazon':
   amazon= input('Search: ')
   webbrowser.open('https://www.amazon.in/s?k=' + amazon)