Sub Stock():
'Allows ws to display the correct info for each worksheet
For Each ws In Worksheets


'Variable Declarations
Dim ColumnTicker As Double
Dim UniqueTotal As Double
Dim ChangeCounter As Double
Dim DateColumn As Double
Dim OpenPrice As Double
Dim ClosingPrice As Double
Dim Yearly As Double
Dim Percent As Double
Dim Total As Double
Dim LastRow As Double
Dim VolumeColumn As Double
Dim Volume As Double
Dim RowNumber As Double
Dim ChallengeColumn As Double
Dim TickerChallenge As Double
Dim ValueChallenge As Double
Dim i As Long
Dim j As Long
Dim k As Long
Dim l As Long
Dim Active As Worksheet


'Static Variable Declarations. These are mainly used as Column trackers
'within loops.  The only exception is RowNumber which uses the second
'row as a default to accomodate for headers.

LastRow = 100000 'This was used for testing after having several overflow
'errors occur.  The next LastRow declaration overrides it.
LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row + 1
ColumnTicker = 1
RowNumber = 2
DateColumn = 2
OpenPrice = 3
ClosingPrice = 6
VolumeColumn = 7
UniqueTicker = 9
Yearly = 10
Percent = 11
Total = 12
ChallengeColumn = 15
TickerChallenge = 16
ValueChallenge = 17


'Dynamic Variable Declarations.  These will all increase through
'loop iterations.

Volume = 0
ChangeCounter = 0
UniqueTotal = 1


'Header and Challenge Requirements Declarations.  This first line
'is also used to wipe I1 to Q(LastRow) to eliminate any leftover
'errors from previous runs of the data.

ws.Range("I1:Q" & LastRow).ClearContents
ws.Cells(1, UniqueTicker).Value = "Ticker"
ws.Cells(1, Yearly).Value = "Yearly Change"
ws.Cells(1, Percent).Value = "Percent Change"
ws.Cells(1, Total).Value = "Total Stock Volume"
ws.Cells(2, ChallengeColumn).Value = "Greatest % Increase"
ws.Cells(3, ChallengeColumn).Value = "Greatest % Decrease"
ws.Cells(4, ChallengeColumn).Value = "Greatest Total Volume"
ws.Cells(1, TickerChallenge).Value = "Ticker"
ws.Cells(1, ValueChallenge).Value = "Value"


'This loop tracks the first column (ColumnTicker) until it finds 2 rows where the
'Ticker is no equal.

For i = 2 To LastRow
    If ws.Cells(i + 1, ColumnTicker).Value <> ws.Cells(i, ColumnTicker).Value Then
    UniqueTotal = UniqueTotal + 1 'Used to keep track of how many unique Stocks are found.
    Volume = Volume + ws.Cells(i, VolumeColumn) 'Sets accumulated total volume of Stock.
    ws.Cells(UniqueTotal, UniqueTicker).Value = ws.Cells(i, ColumnTicker).Value 'Displays Stock ticker.
    ws.Cells(RowNumber, Total).Value = Volume 'Displays Stock Total Volume at I(RowNumber).
    ws.Cells(UniqueTotal, Yearly).NumberFormat = "0.000000000" 'Formating.
    ws.Cells(UniqueTotal, Percent).NumberFormat = "0.00%" 'Formating.
    ws.Range("Q2:Q3").NumberFormat = "0.00%" 'Formating.
    ws.Cells(UniqueTotal, 8).Value = ws.Cells(i - ChangeCounter, OpenPrice).Value 'These are stored for later purposes.
    ws.Cells(UniqueTotal, 13).Value = ws.Cells(i, ClosingPrice).Value 'These are stored for later purposes.
    'This calculates the difference from Closing Price to Opening Price.
    ws.Cells(UniqueTotal, Yearly).Value = ws.Cells(i, ClosingPrice).Value - ws.Cells(i - ChangeCounter, OpenPrice).Value
    RowNumber = RowNumber + 1 'Increments RowNumber for proper positioning in spreadsheet.
    Volume = 0 'Reset when final stock row hits if condition.
    ChangeCounter = 0 'Reset when final stock row hits if condition.
    Else
    'This accumulates the volume for each Stock
    Volume = Volume + ws.Cells(i, VolumeColumn).Value
    'This is used for calculating the position of the opening price for each Stock
    ChangeCounter = ChangeCounter + 1
    End If
Next i
    
    
'This sets the Interior Color of the Yearly Change Column to green if 0% or positive change
'and red if negative change from opening and closing of stock price.

For j = 2 To UniqueTotal 'UniqueTotal is kept to use as the correct row end point for each worksheet.
    If ws.Cells(j, Yearly).Value >= 0 Then
    ws.Cells(j, Yearly).Interior.ColorIndex = 4
    Else
    ws.Cells(j, Yearly).Interior.ColorIndex = 3
    End If
Next j


'This loop is a workaround for determining the percent change when a stock has an opening price
'of 0.  Using something like WorksheetFunction.IfError() should work for this but I could not get
'it to work properly over multiple worksheets so this workaround temporarily stores the
'opening and closing prices for each unique Stock in columns H = 8 and M = 13 (as noted in the i
'loop) to correctly calculate Percent Change for all Stocks.  A similar issue occured while trying
'to calculate the min and max Percent Change for the challenge part as functions like
'Worksheetfunction.Max() were not working properly over multiple worksheets.

For k = 2 To UniqueTotal
    If ws.Cells(k, 8).Value <> 0 Then
    ws.Cells(k, Percent).Value = (ws.Cells(k, 13) - ws.Cells(k, 8)) / ws.Cells(k, 8)
    Else
    ws.Cells(k, Percent).Value = ws.Cells(k, 13) 'Sets the Percentage = Value of Closing Price
    End If
Next k

'These two last commands clear the two columns where the opening and closing prices are stored as
'they are no longer needed.

ws.Range("H1:H" & LastRow).ClearContents
ws.Range("M1:M" & LastRow).ClearContents

Next ws 'Required for each sheet to be ulitized for calculations
End Sub
