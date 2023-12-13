# LING-L555 FINAL PROJECT: Automated Chinese Tone Plotting

## Zach Campbell; Indiana University

## Introduction
My final project will focus on the live plotting and visualization of Standard Mandarin tones. Mandarin Chinese courses at Indiana University place heavy emphasis on early learning and correction of the four tones used in the language Having gone through the courses myself and struggling with my tone realizations, I dreading having to wait till class time for an instructor to judge my tones. Earlier this year I was introduced to PRAAT and the ability to convert data from PRAAT into a tone chart. This process was labor intensive and time consuming. An automated process would aid in research and student learning.

## Scripts for Automating Chinese Tone Analysis
THIS PROJECT IS BY ZACH CAMPBELL FOR LING-L555 FINAL PROJECT
Project Description:
The goal of this project was the automate a long and tedious task of plotting Chinese Tones using PRAAT and Excel. The inital process was outlined in an "Intro to Chinese Linguistics" assignment packet tittled "Plotting Tones Using PRAAT" by Dr. Charles Lin of the IU EALC department. My project resulted in the creation of two scripts: 

## ToPitchSimple.praat
This Script:

    Read from file: "/Users/zachcampbell/LING-L555/project/ExampleToneAudio.wav"
    View & Edit
    Time: Select: 0, 5
    Pitch listing
    Write to file: "/Users/zachcampbell/LING-L555/project/PitchValue.txt"

This script aids in extraction of pitch values of a given recording using PRAAT scripts. This script reads from an existing audio file "/users/your/audio/file/path.wav" and guides the PRAAT program through the PRAAT UI to extract Pitch values at all times in the recording. The writes them to a .txt file "/users/your/text/file.txt".
Running this Script:
1. Download ToPitchSimple.praat to desired location on your computer
2. Open or download and open PRAAT program
3. Select 'Praat' -> 'Open praat script...' -> Open "ToPitchSimple.praat"
4. In praat shell, modify file paths to the location of your audio file and the desired location of your .txt output file
5. Select 'Run' inside praat shell
6. Find and Open produced .txt file with Pitch Values listed inside
7. Optional: Copy entire Pitch Values from file and read below to use PraatPitchToPlot.osts to plot values and visulize tone.

## PraatPitchToPlot.osts
This Script:

   function main(workbook: ExcelScript.Workbook) {
    let selectedSheet = workbook.getActiveWorksheet();
    // Text to columns
    for (let row = 0; row < selectedSheet.getRange("A1:A200").getRowCount(); row++) {
        let sourceRange = selectedSheet.getRange("A1:A200");
        let destinationRange = selectedSheet.getRange("A1");
        let sourceRangeValues = sourceRange.getRow(row).getValues()[0][0].toString().split(/[\t ]/)
        destinationRange.getOffsetRange(row, 0).getResizedRange(0, sourceRangeValues.length - 1).setValues([sourceRangeValues]);
    }
    // Replace "--undefined--" with ""
    selectedSheet.replaceAll("--undefined--", "", { completeMatch: false, matchCase: false });
    // Insert chart and Plot
    let chart_3 = selectedSheet.addChart(ExcelScript.ChartType.line, selectedSheet.getRange("C:C"));
}


This script plots the extracted pitch values from PRAAT using Microsoft Excel script. This script first uses the 'Text to Columns' function to separate the given data into two columns of Time and Hertz values. It then uses the 'Find and Replace' function to find "--undefined--" values, often given with selections from PRAAT, and replaces it with a blank cell. It then plots the pitch values from column C:C into a line graph. 
Note: This script is designed for single syllable/tone plotting and is set with a data range limit of A1:A200. For a data set exceeding A1:A200, simply change the "A200" on lines 4 & 5 to the required range. example: "A1:A200" -> "A1:A350".
Running this Script:
1. Open an Excel worksheet
2. Paste the copied PRAAT 'Pitch Listing' values into cell 'A1'
3. 'Automate' -> 'New Script' -> Delete code in given script -> Copy & Paste "PraatPitchToPlot.osts" code -> 'Run'
4. Optional: 'Save Script' for future use
5. View plotted Pitch Values

## References
This project was completed with guidance and help from the following sources:
    Chun, Dorothy, Jiang, Yan,  ́Avila Reyes, Natalia. (2012). Visualization of
        tone for learning Mandarin Chinese.

    Ring, Hiram. 2017. Analyze Tone and Plot: A Praat script for tonal exploration
        and analysis

    Lin, CHarles. 2023. Using PRAAT to Plot Chinese Tones. Lecture Slides. Indiana University Bloomington.

    PRAAT Manual. 2023. pp.1-360.

