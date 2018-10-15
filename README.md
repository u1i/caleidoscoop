# Caleidoscoop - An API enabled Presentation System

Allow your scripts to use APIs for pushing content such as images, videos, markdown so you can see live updates in a browser window.

## What can you do with this?

You can easily build a kiosk display system with this to show videos and images dynamically on the big screen. Or, how about having all the students in your classroom look at the same material the moment you want them to? You might even use Caleidoscoop to do web presentations for large, distriburted audiences!

## How it works

Users get a minimal HTML page that automatically refreshes when that display receives a new command to show a certain image, video, or markdown document. Your scripts and systems can make authenticated API calls to trigger those changes. Caleidoscoop uses [Bambleweeny](https://github.com/u1i/bambleweeny) as a storage, delivery and API engine.
 
![](https://raw.githubusercontent.com/u1i/caleidoscoop/master/img/c10p-diagram1.png)

## Creating a new display is simple

![](https://raw.githubusercontent.com/u1i/caleidoscoop/master/img/view1.png)

## New display, ready for action

![](https://raw.githubusercontent.com/u1i/caleidoscoop/master/img/view2.png)

## Update the key in B9y to set new content

`echo '{"type":"image","content":"http://blub.krash.net/katong.jpg","height":"0","width":"0"}' | curl -X PUT -d @- http://b9y/keys/$key -H $AUTH`

And just a moment later, the browser window refreshes automatically:

![](https://raw.githubusercontent.com/u1i/caleidoscoop/master/img/view3.png)

