let explanation_correct_header = "<h2>Correct!</h2>";
let explanation_wrong_header = "<h2 class='incorrect-info'>Incorrect!</h2>";
var header = "";

function answer01(){
    $("#option-wrap01 input").attr("disabled","disabled");
    if(document.getElementById("true1").checked){
        header = explanation_correct_header;
    }
    else {
        header = explanation_wrong_header;
    }
    document.getElementById("form1").innerHTML = "<div class='info-block correct-info'>" +
        header +
        "<p>Taking steps to use less electricity, especially when " +
        "it comes from burning coal or gas, can take a big dent out of " +
        "<a href='https://www.britannica.com/science/greenhouse-gas'>greenhouse gas emissions</a>. " +
        "Worldwide, electricity use is responsible for a quarter of all emissions.</p>" +
        "</div>";
    // cited from https://scied.ucar.edu/learning-zone/climate-solutions/reduce-greenhouse-gases
    document.getElementById("general-continue-btn").style.display = "block";
}

function answer02(){
    $("#option-wrap02 input").attr("disabled","disabled");
    if(document.getElementById("true2").checked){
        header = explanation_correct_header;
    }
    else {
        header = explanation_wrong_header;
    }
    document.getElementById("form2").innerHTML = "<div class='info-block correct-info'>" +
        header +
        "<p>Today, about a fifth of global carbon emissions come from raising farm " +
        "animals for meat. For example, as cattle digest food, they burp, releasing methane, " +
        "a powerful greenhouse gas, and their manure releases the greenhouse gases carbon dioxide " +
        "and nitrous oxide. And forests, which take " +
        "<a href='https://www.airthings.com/en-gb/what-is-carbon-dioxide'>carbon dioxide</a> " +
        "out of the air, are often cut " +
        "down so that cattle have space to graze.</p>" +
        "</div>";
    // cited from https://scied.ucar.edu/learning-zone/climate-solutions/reduce-greenhouse-gases
    document.getElementById("general-continue-btn").style.display = "block";
}

function answer03(){
    $("#option-wrap03 input").attr("disabled","disabled");
    if(document.getElementById("true3").checked){
        header = explanation_correct_header;
    }
    else {
        header = explanation_wrong_header;
    }
    document.getElementById("form3").innerHTML = "<div class='info-block correct-info'>" +
        header +
        "<p>More than a third of food produced globally never makes it to the table. " +
        "Some of this wasted food spoils in transit, while consumers throw some of this food out. " +
        "Food loss and waste account for around 8.2 percent of the total human-made greenhouse " +
        "gas emissions.</p>" +
        "</div>";
    // cited from https://www.earthday.org/the-climate-change-quiz/
    document.getElementById("general-continue-btn").style.display = "block";
}

function answer04(){
    $("#option-wrap04 input").attr("disabled","disabled");
    if(document.getElementById("true4").checked){
        header = explanation_correct_header;
    }
    else {
        header = explanation_wrong_header;
    }
    document.getElementById("form4").innerHTML = "<div class='info-block correct-info'>" +
        header +
        "<p>In December 2015, global leaders met in Paris to hash out a climate deal. " +
        "Negotiated under the aegis of the un, it aims to hold the increase in the global " +
        "average temperature to “well below” 2°C above pre-industrial levels. " +
        "The agreement underpins the cop26 climate talks in Glasgow. " +
        "At its heart is a “ratchet mechanism” which requires that every five years parties to the " +
        "agreement come forward with more ambitious national climate goals." +
        "As a consequence, cop26 is the most important climate meeting since Paris " +
        "(it was delayed by a year owing to the pandemic). " +
        "Annotations below, written by our climate team, explain the Paris agreement’s most " +
        "significant elements and point to our related coverage.</p>" +
        "</div>";
    // cited from https://www.economist.com/interactive/paris-climate-agreement-annotated/?gclid=CjwKCAiAs
    // 92MBhAXEiwAXTi2574tGLjFDhXnU6Majmff29XEtPBCh0Vd9ffKFHhVQ7FWdnHW0Inn4RoCIesQAvD_BwE&gclsrc=aw.ds
    document.getElementById("general-continue-btn").style.display = "block";
}

function answer05(){
    $("#option-wrap05 input").attr("disabled","disabled");
    if(document.getElementById("true5").checked){
        header = explanation_correct_header;
    }
    else {
        header = explanation_wrong_header;
    }
    document.getElementById("form5").innerHTML = "<div class='info-block correct-info'>" +
        header +
        "<p>Yes, the effect of rising carbon dioxide on global temperatures reduces as concentration increases. " +
        "We call this a logarithmic relationship, which happens because there is a saturation effect and " +
        "it becomes increasingly difficult for carbon dioxide to influence the climate." +
        "It’s important to remember that we build this model into our projections. " +
        "We understand the relationship between atmospheric carbon dioxide concentrations " +
        "and their effects (as radiative forcing). There is a formula for this relationship, " +
        "seen in the Third Assessment Report from the" +
        "<a href='https://www.ipcc.ch'> Intergovernmental Panel on Climate Change (IPCC)</a>, " +
        "first published in 2001." +
        "In short, we know that more and more carbon dioxide will have less of an effect over time," +
        " but there can still be significant effects on the world before then. </p>"+
        "</div>";
    // cited from https://www.metoffice.gov.uk/weather/climate-change/climate-change-questions
    document.getElementById("general-continue-btn").style.display = "block";
}

function answer06(){
    $("#option-wrap06 input").attr("disabled","disabled");
    if(document.getElementById("optionD6").checked){
        header = explanation_correct_header;
    }
    else {
        header = explanation_wrong_header;
    }
    document.getElementById("form6").innerHTML = "<div class='info-block correct-info'>" +
        header +
        "<p>Greenhouse gases may be a result of natural occurrence or human activity. " +
        "These gases include carbon dioxide (CO2), methane (CH4), water vapor, nitrous oxide (N2O) and ozone (O3). " +
        "Fluorinated gases are also considered to be greenhouse gases. " +
        "Greenhouse gases act like a heat-trapping blanket, making the Earth habitable for humans. " +
        "However, human activities have increased emissions of greenhouse gases into the atmosphere" +
        " beyond what the Earth can support, resulting in climate change.</p>"+
        "</div>";
    // cited from https://www.acs.org/content/acs/en/climatescience/greenhousegases/whichgases.html
    document.getElementById("general-continue-btn").style.display = "block";
}

function answer07(){
    $("#option-wrap07 input").attr("disabled","disabled");
    if(document.getElementById("optionB7").checked){
        header = explanation_correct_header;
    }
    else {
        header = explanation_wrong_header;
    }
    document.getElementById("form7").innerHTML = "<div class='info-block correct-info'>" +
        header +
        "<p>The Earth receives solar radiation from the sun. " +
        "Passing through the atmosphere, some radiation is absorbed by the Earth, " +
        "while some is reflected back to space. When the exchange of incoming and outgoing radiation occurs, " +
        "some of the radiation becomes trapped by gases in the atmosphere. " +
        "This creates a “greenhouse” effect and warms the planet.</p>"+
        "</div>";
    // cited from https://www.earthday.org/the-climate-change-quiz/
    document.getElementById("general-continue-btn").style.display = "block";
}

function answer08(){
    $("#option-wrap08 input").attr("disabled","disabled");
    if(document.getElementById("optionA8").checked){
        header = explanation_correct_header;
    }
    else {
        header = explanation_wrong_header;
    }
    document.getElementById("form8").innerHTML = "<div class='info-block correct-info'>" +
        header +
        "<p>In december 2015, global leaders met in Paris to hash out a climate deal. " +
        "Negotiated under the aegis of the un, it aims to hold the increase in the " +
        "global average temperature to “well below” 2°C above pre-industrial levels. " +
        "The agreement underpins the cop26 climate talks in Glasgow. At its heart is a “ratchet mechanism”" +
        " which requires that every five years parties to the agreement come forward " +
        "with more ambitious national climate goals. As a consequence, cop26 is the most " +
        "important climate meeting since Paris (it was delayed by a year owing to the pandemic). " +
        "Annotations below, written by our climate team, explain the Paris agreement’s most " +
        "significant elements and point to our related coverage.</p>"+
        "</div>";
    // cited from https://www.economist.com/interactive/paris-climate-agreement-annotated/?gclid=
    // CjwKCAiAs92MBhAXEiwAXTi2574tGLjFDhXnU6Majmff29XEtPBCh0Vd9ffKFHhVQ7FWdnHW0Inn4RoCIesQAvD_BwE&gclsrc=aw.ds
    document.getElementById("general-continue-btn").style.display = "block";
}

function answer09(){
    $("#option-wrap09 input").attr("disabled","disabled");
    if(document.getElementById("optionD9").checked){
        header = explanation_correct_header;
    }
    else {
        header = explanation_wrong_header;
    }
    document.getElementById("form9").innerHTML = "<div class='info-block correct-info'>" +
        header +
        "<p>Humans cause climate change by releasing carbon dioxide and other greenhouse gases into the air. " +
        "Today, there is more carbon dioxide in the atmosphere than there ever has been in at least " +
        "the past 2 million years. During the 20th and 21st century, " +
        "the level of carbon dioxide rose by 40%.</p>"+
        "</div>";
    // cited from https://www.metoffice.gov.uk/weather/climate-change/causes-of-climate-change
    document.getElementById("general-continue-btn").style.display = "block";
}

function answer10(){
    $("#option-wrap10 input").attr("disabled","disabled");
    if(document.getElementById("optionE10").checked){
        header = explanation_correct_header;
    }
    else {
        header = explanation_wrong_header;
    }
    document.getElementById("form10").innerHTML = "<div class='info-block correct-info'>" +
        header +
        "<p> We produce greenhouse gases in lots of different ways:" +
        "Burning fossil fuels – Fossil fuels such as oil, gas, and coal contain carbon dioxide " +
        "that has been 'locked away' in the ground for thousands of years. " +
        "When we take these out of the land and burn them, we release the stored carbon dioxide into the air." +
        "Deforestation – Forests remove and store carbon dioxide from the atmosphere. " +
        "Cutting them down means that carbon dioxide builds up quicker since there are no trees to absorb it. " +
        "Not only that, trees release the carbon they stored when we burn them.</p>"+
        "</div>";
    // cited from https://www.metoffice.gov.uk/weather/climate-change/causes-of-climate-change
    document.getElementById('general-next-btn').style.display = "none";
}

function answer11(){
    $("#option-wrap11 input").attr("disabled","disabled");
    if(document.getElementById("false11").checked){
        header = explanation_correct_header;
    }
    else {
        header = explanation_wrong_header;
    }
    document.getElementById("form11").innerHTML = "<div class='info-block correct-info'>" +
        header +
        "<p>Reducing food waste can make an even larger impact, saving about 90 gigatons of " +
        "carbon dioxide from " +
        "<a href='https://www.nationalgeographic.org/encyclopedia/atmosphere/'>the atmosphere</a> " +
        "over 30 years.</p>"+
        "</div>";
    // cited from https://scied.ucar.edu/learning-zone/climate-solutions/reduce-greenhouse-gases
    document.getElementById("advance-continue-btn").style.display = "block";
}

function answer12(){
    $("#option-wrap12 input").attr("disabled","disabled");
    if(document.getElementById("false12").checked){
        header = explanation_correct_header;
    }
    else {
        header = explanation_wrong_header;
    }
    document.getElementById("form12").innerHTML = "<div class='info-block correct-info'>" +
        header +
        "<p>It would make sense for the " +
        "<a href='https://climate.nasa.gov/causes/'>climate to change </a>" +
        "if the Sun got hotter, " +
        "but we have seen no evidence to suggest this is happening.</p>"+
        "</div>";
    // cited from https://www.metoffice.gov.uk/weather/climate-change/climate-change-questions
    document.getElementById("advance-continue-btn").style.display = "block";
}

function answer13(){
    $("#option-wrap13 input").attr("disabled","disabled");
    if(document.getElementById("false13").checked){
        header = explanation_correct_header;
    }
    else {
        header = explanation_wrong_header;
    }
    document.getElementById("form13").innerHTML = "<div class='info-block correct-info'>" +
        header +
        "<p>People often suggest that periods of warming and cooling show that the global climate " +
        "wasn’t stable before " +
        "<a href='https://www.landmarkacademyhub.co.uk/climate-change-impacts-of-the-industrial-revolution/'>" +
        "the Industrial Revolution.</a> " +
        "Examples include the ‘Roman Warm Period’, the ‘Medieval Warm Period’ and the ‘Little Ice Age’. " +
        "The difference is that these events were regional, and only affected parts of the world. " +
        "This is an important distinction, because what we see today is a period where most of the " +
        "globe is warming at the same time. The Roman and Medieval warm periods only affected " +
        "the North Atlantic region..</p>"+
        "</div>";
    // cited from https://www.metoffice.gov.uk/weather/climate-change/climate-change-questions
    document.getElementById("advance-continue-btn").style.display = "block";
}

function answer14(){
    $("#option-wrap14 input").attr("disabled","disabled");
    if(document.getElementById("true14").checked){
        header = explanation_correct_header;
    }
    else {
        header = explanation_wrong_header;
    }
    document.getElementById("form14").innerHTML = "<div class='info-block correct-info'>" +
        header +
        "<p>Cows and sheep produce large amounts of methane when they digest their food.</p>"+
        "</div>";
    // cited from https://ec.europa.eu/clima/climate-change/causes-climate-change_en
    document.getElementById("advance-continue-btn").style.display = "block";
}

function answer15(){
    $("#option-wrap15 input").attr("disabled","disabled");
    if(document.getElementById("true15").checked){
        header = explanation_correct_header;
    }
    else {
        header = explanation_wrong_header;
    }
    document.getElementById("form15").innerHTML = "<div class='info-block correct-info'>" +
        header +
        "<p><a href='https://ec.europa.eu/clima/eu-action/fluorinated-greenhouse-gases_en'>Fluorinated gases</a> " +
        "are emitted from equipment and products that use these gases. " +
        "Such emissions have a very strong warming effect, up to 23 000 times greater than CO2.</p>"+
        "</div>";
    // cited from https://ec.europa.eu/clima/climate-change/causes-climate-change_en
    document.getElementById("advance-continue-btn").style.display = "block";
}

function answer16(){
    $("#option-wrap16 input").attr("disabled","disabled");
    if(document.getElementById("optionC16").checked){
        header = explanation_correct_header;
    }
    else {
        header = explanation_wrong_header;
    }
    document.getElementById("form16").innerHTML = "<div class='info-block correct-info'>" +
        header +
        "<p>Today, the amount of electricity that comes from " +
        "<a href='https://www.eia.gov/energyexplained/what-is-energy/sources-of-energy.php'>renewable energy</a>" +
        " is growing." +
        "A few countries, such as Iceland and Costa Rica, now get nearly all of their electricity " +
        "from renewable energy. In many other countries, the percentage of electricity from " +
        "renewable sources is currently small (5-10%) but growing.</p>"+
        "</div>";
    // cited from https://scied.ucar.edu/learning-zone/climate-solutions/reduce-greenhouse-gases
    document.getElementById("advance-continue-btn").style.display = "block";
}

function answer17(){
    $("#option-wrap17 input").attr("disabled","disabled");
    if(document.getElementById("optionC17").checked){
        header = explanation_correct_header;
    }
    else {
        header = explanation_wrong_header;
    }
    document.getElementById("form17").innerHTML = "<div class='info-block correct-info'>" +
        header +
        "<p> Most of the ways we have to get from place to place currently rely on fossil " +
        "fuels - gasoline for vehicles and jet fuel for planes. Burning fossil fuels for " +
        "transportation adds up to 14% of global greenhouse gas emissions worldwide. " +
        "We can reduce emissions by shifting to alternative technologies that either " +
        "don’t need gasoline (like bicycles and electric cars) or don’t need as much (like hybrid cars). " +
        "Using public transportation, carpooling, biking, and walking, leads to fewer vehicles " +
        "on the road and less greenhouse gases in the atmosphere. " +
        "Cities and towns can make it easier for people to lower greenhouse gas emissions by " +
        "adding bus routes, bike paths, and sidewalks. </p>"+
        "</div>";
    // cited from https://scied.ucar.edu/learning-zone/climate-solutions/reduce-greenhouse-gases
    document.getElementById("advance-continue-btn").style.display = "block";
}

function answer18(){
    $("#option-wrap18 input").attr("disabled","disabled");
    if(document.getElementById("optionC18").checked){
        header = explanation_correct_header;
    }
    else {
        header = explanation_wrong_header;
    }
    document.getElementById("form18").innerHTML = "<div class='info-block correct-info'>" +
        header +
        "<p> Humans cause climate change by releasing carbon dioxide and other " +
        "greenhouse gases into the air. Today, there is more carbon dioxide in the " +
        "atmosphere than there ever has been in at least the past 2 million years. " +
        "During the 20th and 21st century, the level of carbon dioxide rose by 40%.</p>"+
        "</div>";
    // cited from https://www.metoffice.gov.uk/weather/climate-change/causes-of-climate-change
    document.getElementById("advance-continue-btn").style.display = "block";
}

function answer19(){
    $("#option-wrap19 input").attr("disabled","disabled");
    if(document.getElementById("optionC19").checked){
        header = explanation_correct_header;
    }
    else {
        header = explanation_wrong_header;
    }
    document.getElementById("form19").innerHTML = "<div class='info-block correct-info'>" +
        header +
        "<p>The leading cause of climate change is human activity and the release of greenhouse gases. " +
        "However, there are lots of natural causes that also lead to changes in the climate system." +
        "Natural cycles can cause the climate to alternate between warming and cooling. " +
        "There are also natural factors that force the climate to change, known as 'forcings'. " +
        "Even though these natural causes contribute to climate change, we know that they are " +
        "not the primary cause, based on scientific evidence." +
        "Some of these natural cycles include: Milankovitch cycles – " +
        "As Earth travels around the sun, its path and the tilt of its axis can change slightly. " +
        "These changes, called Milankovitch cycles, affect the amount of sunlight that falls on Earth. " +
        "This can cause the temperature of Earth to change.</p>"+
        "</div>";
    // cited from https://ec.europa.eu/clima/climate-change/causes-climate-change_e
    document.getElementById("advance-continue-btn").style.display = "block";
}


function answer20(){
    $("#option-wrap20 input").attr("disabled","disabled");
    if(document.getElementById("optionB20").checked){
        header = explanation_correct_header;
    }
    else {
        header = explanation_wrong_header;
    }
    document.getElementById("form20").innerHTML = "<div class='info-block correct-info'>" +
        header +
        "<p> 2011-2020 was the warmest decade recorded, with global average temperature reaching 1.1°C " +
        "above pre-industrial levels in 2019. Human-induced global warming is presently increasing " +
        "at a rate of 0.2°C per decade. </p>"+
        "</div>";
    // cited from https://ec.europa.eu/clima/climate-change/causes-climate-change_en
    document.getElementById('advance-next-btn').style.display = "none";
}

function enable_all(){
    $(":input").attr("disabled",false)
}


function listener_activate_btn1(){
    var continue_btn1 = document.getElementById("general-continue-btn");

    continue_btn1.addEventListener('click',function(){
        continue_btn1.style.display = "none";
    });

}

function listener_activate_btn2(){
    var continue_btn2 = document.getElementById("advance-continue-btn");
    continue_btn2.addEventListener('click',function(){
        continue_btn2.style.display = "none";
    });
}
document.addEventListener('readystatechange', function (){
    listener_activate_btn1();
});

document.addEventListener('readystatechange', function (){
    listener_activate_btn2();
});

function pop_window(){
    var create_account = confirm("Do you want to store your score? \n" +
                                "Sign up an account and then store your quiz mark. ");
    var host = window.location.host;
    if (create_account){
        window.location.href= "http://"+ host + "/register";
    }
    else {
        window.location.href= "http://"+ host + "/quiz";
    }
}




