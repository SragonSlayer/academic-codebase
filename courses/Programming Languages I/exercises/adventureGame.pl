/*
This is a little adventure game. There are three entities: you, a treasure, and an ogre. 
There are six places: a valley, a path, a cliff, a fork, a maze, and a mountaintop. 
Your goal is to get the treasure without being killed first.
*/


/*
First, text descriptions of all the places in the game.
*/
 description(valley,'You are in a pleasant valley, with a trail ahead.'). 
 description(path,'You are on a path, with ravines on both sides.'). 
 description(cliff,'You are teetering on the edge of a cliff.'). 
 description(fork,'You are at a fork in the path.'). 
 description(maze(_), 'You are in a maze of twisty trails, all alike.'). 
 description(mountaintop, 'You are on the mountaintop.').
 description(gate, 'You arrive at a gate leading to the mountaintop, and the treasure within. This is your last obstacle before victory! You may type "backward." if you do not posess the key. What you seek lies within the maze!').

/*
These connect predicates establish the map. The meaning of connect(X,Dir,Y) is that if you are at X and you move in direction Dir, you get to Y. Recognized directions are forward, right, and left.
*/
connect(valley,forward,path). 
connect(path,right,cliff). 
connect(path,left,cliff). 
connect(path,forward,fork). 
connect(fork,left,maze(0)). 
connect(fork,right,gate). 
connect(gate, forward, mountaintop).
connect(gate, backward, fork).
connect(maze(0),left,maze(1)). 
connect(maze(0),right,maze(3)). 
connect(maze(1),left,maze(0)). 
connect(maze(1),right,maze(2)). 
connect(maze(2),left,fork). 
connect(maze(2),right,maze(0)). 
connect(maze(3),left,maze(0)). 
connect(maze(3),right,maze(3)).


/*
move(forward) when at the gate and it is locked, prints a message and does not move.
*/
move(forward) :-
    at(you,gate),
    gate(locked),
    write('The gate is locked! to unlock the gate type unlock.\n'),
    report, 
    !.

/*
move(forward) when you pass the gate with the key still you are struck by lightning!.
*/
move(forward) :-
    at(you,gate),
    gate(unlocked),
    carrying(you, key),
    write('As you pass through the gate with the key in your possession, a bolt of lightning strikes you down for your hubris!\nYou lose this round. Try Again! \n'),
    retract(at(you,gate)), 
    assert(at(you,done)),
    !.
/*
move(Dir) moves you in direction Dir, then prints the description of your new location.
*/
move(Dir) :-
    at(you,Loc),
    connect(Loc,Dir,Next), 
    retract(at(you,Loc)), 
    assert(at(you,Next)), 
    report, 
    !.

/*
But if the argument was not a legal direction, print an error message and don't move.
*/ 
move(_) :- write('That is not a legal move.\n'), report.

/*
unlock. will unlock the gate if you are at the gate and you possess the key.
*/
unlock :-
    gate(locked),
    carrying(you,key),
    retract(gate(locked)),
    assert(gate(unlocked)),
    write('You have unlocked the gate!\n'),
    !.
unlock :- 
    gate(unlocked),
    write('The gate is already unlocked!\n'),
    !.
unlock :-
    write('You cannot unlock the gate without the key!\n'),
    !.

/* 
pickup. picks up the key if you are at the key's location.
*/
pickup :-
    at(you,Loc),
    at(key,Loc),
    carrying(you,nothing),
    retract(at(key,Loc)),
    assert(carrying(you,key)),
    write('You have picked up the key.\n'),
    !.
pickup :-
    write('There is no key here\n'),
    !.

/*
putdown. puts down the key at the your location.
*/
putdown :- 
    carrying(you,key),
    at(you,Loc),
    assert(at(key,Loc)),
    retract(carrying(you,key)),
    assert(carrying(you,nothing)),
    write('You have put down the key.\n'),
    !.
putdown :-
    write('You do not have anything to put down\n'),
    !.

/* Shorthand for moves. */
forward :- move(forward). 
left :-move(left). 
right :-move(right). 
backward :- move(backward).


/*
report prints the description of your current location.
*/ 
report :- 
    at(you,X),
    at(key,X),
    write('There is a key here. You may pick it up here with pickup.\n'),
    !.
report :- 
    at(you,X), 
    description(X,Y), 
    write(Y), nl.

/*
If you and the ogre are at the same place, it kills you.
*/ 
ogre :- 
    at(ogre,Loc), 
    at(you,Loc),
    write('An ogre sucks your brain out through\n'),
     write('your eye sockets, and you die.\n'), 
     retract(at(you,Loc)), 
     assert(at(you,done)), 
     !.
/*
But if you and the ogre are not in the same place, nothing happens.
*/ 
ogre.

/*
If you and the treasure are at the same place, you win.
*/ 
treasure :-
    at(treasure,Loc), 
    at(you,Loc),
    write('There is a treasure here.\n'), 
    write('Congratulations, you win!\n'), 
    retract(at(you,Loc)), 
    assert(at(you,done)), 
    !.
/* But if you and the treasure are not in the same place, nothing happens. */
treasure. 
/* If you are at the cliff, you fall off and die. */
cliff :- 
    at(you,cliff),
    write('You fall off and die.\n'), 
    retract(at(you,cliff)), 
    assert(at(you,done)), 
    !.
/* But if you are not at the cliff nothing happens. */
cliff.


/* Main loop. Stop if player won or lost. */
main :-
    at(you,done),
    write('Thanks for playing.\n'), 
    !.
/*
Main loop. Not done, so get a move from the user and make it. Then run all our special behaviors. Then repeat.
*/ 
main :-
    write('\nNext move - '), 
    read(Move), 
    call(Move), 
    ogre,
    treasure, 
    cliff, 
    main.

/*
This is the starting point for the game. We assert the initial conditions, print an initial report, then start the main loop.
*/ 
go :-
    retractall(at(_,_)), % clean up from previous runs 
    assert(carrying(you, nothing)),
    assert(gate(locked)),
    assert(at(you,valley)), 
    assert(at(ogre,maze(3))), 
    assert(at(treasure,mountaintop)), 
    assert(at(key, maze(2))),
    write('This is an adventure game. \n'), 
    write('Legal moves are pickup, putdown, left, right, backward, or forward.\n'), 
    write('End each move with a period.\n\n'), 
    report, 
    main.