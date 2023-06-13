from flask import Blueprint, render_template, request
from mario_kart import db
from mario_kart.models import Player

players = Blueprint('players', __name__)

@players.route("/player")
def player():
    player = Player.query.first()
    return player