
<h1>ASU EPICS with Bridge2Africa: Braille Display and Screen Reader</h1>

<p>Bridge2Africa program, in partnership with ASU students, seeks to solve the problem of the non-blind-friendly nature of internet browsing. The internet is a fantastic education tool due to its abundance of information; however, it is mainly accessible and easy to use for sight-based users. 
Blind students have more difficulties taking advantage of these resources, putting them in a deficit from other non-blind students. </p>
<p><b>The goal of this project is to create a Refreshable Braille Display and Screen reader 
software that will aim to help the visually impaired browse the internet</b></p>
<p>This git repo is the screen reading software and the communication software to the microcontroller. The screen reading software is the interface between the user
and the braille display. They use the software to browse the internet and press certain buttons to do different navigation functions and translate certain information
on the screen. This repo also holds the communication software where we have created our own protocol that converts HTML information from the screen into binary
instructions for our braille display to understand</p>

<h3>Link to Design Document: https://docs.google.com/document/d/1ovyGRtFqcLOZ2RKHfSEC2vQF8a79lpYYkmhWrsfVn9o/edit?usp=sharing</h3>
<h3>Demo: https://www.youtube.com/watch?v=_R-REKt_a0I&ab_channel=AdrianeInocencio </h3>
<h3>Running the project</h3>

```bash
# Clone this project
$ git clone https://github.com/adriane0523/Bridge2Africa.git

# Access
$ cd Python_software/src/


# create a virutal enviroment to install your dependencies,
$ python -m venv venv

#activate it you should see (venv)
$ venv/Scripts/activate

#install dependencies
$ pip install -r requirements.txt

#run the app
$ python main.py

#Use arduino ide to lauch the files within Arduino_Software
```

<h3>Progress so far</h3>
Still under development

<h5>Current Wiring of the Braille Display</h5>
<img width="661" alt="Picture2" src="https://user-images.githubusercontent.com/38186787/118159538-f7b05f80-b3d1-11eb-82d9-ab7bce0e67af.png">

<h5>Current Software Decomposition</h5>
<img width="936" alt="Picture1" src="https://user-images.githubusercontent.com/38186787/118159526-f2ebab80-b3d1-11eb-9bea-3c86a2ef7a89.png">
<h5>Current Housing</h5>
<img width="468" alt="Picture3" src="https://user-images.githubusercontent.com/38186787/118159554-fc751380-b3d1-11eb-980e-d9c8c3a243c8.png">
