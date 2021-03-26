#Include Gdip_all.ahk
pToken := Gdip_Startup()

WinActivate, Brushless DC drive
WinWaitActive, Brushless DC drive,, 2
if ErrorLevel {
  MsgBox, Winwait timed out
  return
}

hwnd := WinActive(Brushless DC drive)

Loop, 64 {
  i := A_Index - 1
  file := Format("file{:02}.esp", i)
  screenshot := Format("shot{:02}.png", i)
  Click, 420 110 ; Load File
  Send %file%
  Send {Enter}
  Sleep 1000
  snap := Gdip_BitmapFromScreen("hwnd:" . hwnd)
  Gdip_SaveBitmapToFile(snap, screenshot)
}
