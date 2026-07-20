import os

import chess

from dotenv import load_dotenv

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

from game import ChessGame
from board import square_text



load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


games = {}





def chess_keyboard(board):

    keyboard = []


    for rank in range(7, -1, -1):

        row = []


        for file in range(8):

            square = chess.square(
                file,
                rank
            )


            row.append(

                InlineKeyboardButton(

                    square_text(
                        board,
                        square
                    ),

                    callback_data=f"sq_{square}"

                )

            )


        keyboard.append(row)



    keyboard.append(

        [
            InlineKeyboardButton(
                "🔄 بازی جدید",
                callback_data="new"
            ),

            InlineKeyboardButton(
                "🏳 تسلیم",
                callback_data="giveup"
            )
        ]

    )


    return InlineKeyboardMarkup(keyboard)








async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):


    user_id = update.effective_user.id


    games[user_id] = ChessGame()



    await update.message.reply_text(

        "♟️ Astra Chess شروع شد!\n"
        "حرکت کن:",

        reply_markup=chess_keyboard(
            games[user_id].board
        )

    )








async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):


    query = update.callback_query

    await query.answer()


    user_id = query.from_user.id


    if user_id not in games:

        games[user_id] = ChessGame()



    game = games[user_id]


    data = query.data





    if data == "new":

        games[user_id] = ChessGame()


        await query.edit_message_text(

            "♟️ بازی جدید شروع شد",

            reply_markup=chess_keyboard(
                games[user_id].board
            )

        )

        return





    if data == "giveup":


        await query.edit_message_text(

            "🏳 بازی را واگذار کردی"

        )

        return







    if data.startswith("sq_"):


        square = int(

            data.split("_")[1]

        )



        if game.selected is None:


            game.selected = square


            await query.edit_message_text(

                "📍 مقصد را انتخاب کن:",

                reply_markup=chess_keyboard(
                    game.board
                )

            )


            return




        else:


            moved = game.player_move(

                game.selected,

                square

            )


            game.selected = None



            if moved:


                if game.game_status() == "Playing":


                    game.bot_move()



            status = game.game_status()



            if status != "Playing":


                await query.edit_message_text(

                    f"🏆 پایان بازی\n\n"
                    f"{status}"

                )

                return




            await query.edit_message_text(

                "♟️ حرکت بعدی:",

                reply_markup=chess_keyboard(
                    game.board
                )

            )








def main():


    app = Application.builder().token(TOKEN).build()


    app.add_handler(

        CommandHandler(
            "start",
            start
        )

    )


    app.add_handler(

        CallbackQueryHandler(play)

    )


    print("Astra Chess Started ♟️")


    app.run_polling()





if __name__ == "__main__":

    main()
