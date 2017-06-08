---
layout: page
title : Links
permalink: /links/
category: "Links"
---

These are links to miscellaneous things that I've enjoyed reading and don't want to lose track of in case I'm looking for it again.

---

***Web Series***

**[XKCD][1]** \- By Randall Munroe and pretty much the source of all the references I make. It also brings up some interesting philosophical questions, and isn't just a comic strip.

**[Order of the Stick][2]** \- A great D&D webcomic that breaks the fourth wall quite frequently, and while it's at it, breaks the third and second walls too. It's pretty funny, but the producer has been suffering a chronic illness and hasn't been updating it as frequently as he used to.

**[Super Powereds][3]** \- An online book series that follows five college students going to a college for super powers. It sounds corny, but is actually quite good, and the exemplary plot more than makes up for the somewhat frequent typos.

---

***Interesting Papers***

**[Large Autonomous Behavior Models][4]** \- I've been struck multiple times with an interest in the seemingly complex behaviors that occur when you create a large number of particles or entities and write a few rules that they have to abide by, and this paper demonstrates some of the simpler strategies for modeling birds and their reactions.

**[Cloud Rendering][5]** \- Clouds are really cool, and at some point I'm going to get around to write some code that generates images of clouds. In the meantime, this paper has helped me think about some of the challenges of rendering a whole ton of particles. They solve it by reducing the number of particles and making each particle take up more space with little Gaussian-distributed dots which reduces the amount of things needed to render, however since I'm not planning on making my code realtime, I can do whatever I want and hopefully come out with an even more realistic result.

**[Extended LQR][6]** \- A _whole_ lot of this went over my head, but as I think about other concepts in control theory, hopefully I'll return to this paper with a better understanding. It's a form of tuning your controller, but a more advanced version of linear-quadratic regulator control, which is already a more complicated method of tuning your controller than simple pole placement.

**[Introduction to Kalman Filters][7]** \- Going with the control theory theme is this paper giving a brief overview of Kalman filters, which can be used in controls to take a noisy system and reduce the noise through an observer, which compares a model of the system to the read position and ends up being _very_ helpful. I'm forever getting a better understanding of controls, so this description might get revised.





[1]:https://xkcd.com
[2]:http://www.giantitp.com/comics/oots0001.html
[3]:http://www.drewhayesnovels.com/superpowereds/
[4]:http://www.red3d.com/cwr/papers/2000/pip.pdf
[5]:http://www.markmark.net/PDFs/RTClouds_HarrisEG2001.pdf
[6]:https://pdfs.semanticscholar.org/7958/d2367c0f1988dbd2b9644ad65f86a8fca98b.pdf
[7]:http://www.cs.unc.edu/~welch/media/pdf/kalman_intro.pdf
