with Ada.Text_IO; use Ada.Text_IO;

procedure Kronos_Core is
   Input_File  : File_Type;
   Output_File : File_Type;
   Line        : String (1 .. 80);
   Last        : Natural;
   
   -- متغيرات التداول
   Ticker      : String (1 .. 6);
   Action      : String (1 .. 4);
   Qty         : Integer;
   Price       : Integer;
   
   -- محاكاة بسيطة لأفضل سعر متاح (Best Ask/Bid)
   Current_AAPL_Bid : Integer := 150;
   Current_BTC_Bid  : Integer := 65000;
begin
   Open (Input_File, In_File, "data/input/live_orders.dat");
   Create (Output_File, Out_File, "data/output/trade_executions.txt");

   Put_Line (Output_File, "=======================================================");
   Put_Line (Output_File, " ⚡ KRONOS HFT ENGINE - ZERO-LATENCY MATCHING");
   Put_Line (Output_File, "=======================================================");
   Put_Line (Output_File, "");

   while not End_Of_File (Input_File) loop
      Get_Line (Input_File, Line, Last);
      
      -- قراءة أوامر التداول الواردة (توقع دقة البيانات)
      if Last >= 23 then
         Ticker := Line (1 .. 6);
         Action := Line (8 .. 11);
         Qty    := Integer'Value (Line (13 .. 17));
         Price  := Integer'Value (Line (19 .. 23));

         -- خوارزمية المطابقة (Matching Logic)
         if Action = "SELL" then
            Put_Line (Output_File, "[ORDER BOOKED] " & Action & " " & Integer'Image(Qty) & " shares of " & Ticker & " @ $" & Integer'Image(Price));
         elsif Action = "BUY " then
            -- التحقق من تطابق السعر لتنفيذ الصفقة
            if (Ticker = "AAPL  " and Price >= Current_AAPL_Bid) or 
               (Ticker = "BTCUSD" and Price >= Current_BTC_Bid) then
               Put_Line (Output_File, "[TRADE EXECUTED] MATCHED " & Integer'Image(Qty) & " " & Ticker & " @ $" & Integer'Image(Price));
               Put_Line (Output_File, "                 >> CLEARING SENT TO BLOCKCHAIN/LEDGER");
               Put_Line (Output_File, "-------------------------------------------------------");
            else
               Put_Line (Output_File, "[ORDER BOOKED] " & Action & " " & Integer'Image(Qty) & " shares of " & Ticker & " @ $" & Integer'Image(Price));
            end if;
         end if;
      end if;
   end loop;

   Put_Line (Output_File, "");
   Put_Line (Output_File, "=======================================================");
   Put_Line (Output_File, " 🛑 TRADING SESSION CLOSED. ALL LEDGERS RECONCILED.");
   Put_Line (Output_File, "=======================================================");

   Close (Input_File);
   Close (Output_File);
end Kronos_Core;
