import sys
# These are the transitions, start state is 0 (See notes)
T = { (0,'clickTriChooseButton'):(1,'showTP'),
      (0,'mouseDownVertex'):(3,'selectV'),
      (0,'clickRecenterButton'):(2,'showCP'),
      (1,'mouseDownVertex'):(3,'hideTP selectV'), # may need to split this later to get both args
      (1,'clickRecenterButton'):(2,'hideTP showCP'),
      (1,'click'):(0,'hideTP'),
      (1,'clickTriChooseButton'):(0,'hideTP'),
      (1,'clickOnCanvas'):(0,'hideTP'),
      (1,'clickTriTypeChoice'):(0,'resetT hideTP'),
      (2,'clickRecenterButton'):(0,'hideCP'),
      (2,'click'):(0,'hideCP'),
      (2,'clickOnCanvas'):(0,'hideCP moveC'),
      (2,'recenterTextChange'):(4,'checkCT'),
      (3,'mouseMove'):(3,'moveV'),
      (3,'mouseUpCanvas'):(0,'noop'),
      (3,'mouseLeaveCanvas'):(0,'resetV'),
      (4,'recenterTextFail'):(2,'errorCT'),
      (4,'recenterTextSucc'):(0,'moveC hideCP'),
      (2,'clickTriChooseButton'):(1,'showTP hideCP'),
      }

if __name__ == "__main__":
    frgui = open("fromGUI","r")
    togui = open("toGUI","w")
    count = 0
    state = 0

    while True:
        # Read event message
        try:
            msg,data = frgui.readline().split(maxsplit=1);
        except:
            break
        count += 1
        print(f'Read({count}): {msg} {data}',file=sys.stderr) #4DEBUG!

        # Choose action message to respond with
        # IMPORTANT! My example code does something silly ...
        # - if you click on a vertex, the "Recentering Pane" will appear,
        #   and when you leave the "canvas", it disappears.  See why?
        response = "noop 0"
        if (state,msg) in T:
            state,response = T[(state,msg)]
            r = response.split()
            for i in r:
                print(i +" "+ data + "\n",file=togui,flush=True)
                print(f'Sent({count}): {i} and state {state}',file=sys.stderr) #4DEBUG!

        else:
            print(response + "\n",file=togui,flush=True)
        
        # Respond to GUI - flush to send line immediately!
        #print(f'Sent({count}): {response} and state {state}',file=sys.stderr) #4DEBUG!
