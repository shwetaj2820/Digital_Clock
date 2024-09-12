//---------------------------------------------------------------------------

#include <fmx.h>
#pragma hdrstop

#include "Unit1.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.fmx"
TForm1 *Form1;
//---------------------------------------------------------------------------
__fastcall TForm1::TForm1(TComponent* Owner)
	: TForm(Owner)
{
}
//---------------------------------------------------------------------------
void __fastcall TForm1::AddButtonClick(TObject *Sender)
{
	String txt = AddTask->Text;
	if(txt == ""){
		
// 		handling the function for empty string entered
	}
	TaskList->Items->Add(txt);
    AddTask->Text="";
}
//---------------------------------------------------------------------------

void __fastcall TForm1::TaskListItemClick(TCustomListBox * const Sender, TListBoxItem * const Item)

{
	int index = Item->Index;
    TaskList->Items->Delete(index);
}
//---------------------------------------------------------------------------

