% Conveyor Library Example
% -------------------------
% 
% .. note::
% 
%     Make sure you have Quanser Interactive Labs open before running this
%     example.  This example is designed to best be run in any of the open
%     world environments.

close all;
clear all;
clc;

fprintf('\n\n------------------------------ Communications --------------------------------\n\n');

qlabs = QuanserInteractiveLabs();
connection_established = qlabs.open('localhost');

if connection_established == false
    disp("Failed to open connection.")
    return
end


disp('Connected')

num_destroyed = qlabs.destroy_all_spawned_actors();

fprintf('%d actors destroyed', num_destroyed);


cylinder = QLabsWidget(qlabs);

% create a camera in this qlabs instance
camera = QLabsFreeCamera(qlabs);

% place the custom camera at a specified location and rotation using radians
camera.spawn([0.8,0.7,1.3],[0,0.8,-1.581]);

% to switch our view from our current camera to the new camera we just initialized to 
% be able to view where our people will spawn
camera.possess();

% The configuration argument is an integer associated with the length of the conveyors
% For straight conveyor, configuration = 0 corresponds to a length of 0.5. With each
% increase in configuration, the lengh is increased by 0.25, up to configuratoin = 20 
straightConveyor = QLabsConveyorStraight(qlabs);
straightConveyor.spawn_id_degrees(0,[0, 0, 0], [0, 0, 0], [1,1,1], 5);

% For curved conveyor, configuration = 0 corresponds to a circular arc of 15 degree. 
% With each increase in configuration, the arc length is increased by 15 degrees, up to 
% configuratoin = 24.
curvedConveyor = QLabsConveyorCurved(qlabs);
curvedConveyor.spawn_id_degrees(1,[0.03, -0.5, 0], [0, 0, 0], [1,1,1], 6);

pause(2);

% set the speed for each conveyor 
straightConveyor.set_speed(0.3);
curvedConveyor.set_speed(0.07);

% drop one cylinder widget on top of the straight convoryer
cylinder.spawn([1.6, 0, 1], [0, 0, 5], [0.05, 0.05, 0.05], cylinder.CYLINDER)

pause(1);

qlabs.close()