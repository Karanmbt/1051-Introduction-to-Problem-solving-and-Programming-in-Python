extends HBoxContainer


# Called when the node enters the scene tree for the first time.
enum modes {SIMPLE, EMPTY, PARTIAL}

var heart_full = preload("res://hud_heartFull.png")
var heart_empty = preload("res://hud_heartEmpty.png")
var heart_half = preload("res://hud_heartHalf.png")

@export var mode : modes

func update_health(value):
	match mode:
		MODES.simple:
			update_simple(value)
		MODES.empty:
			update_empty(value)
		MODES.partial:
			update_partial(value)


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
