function Container = BBeamMakeCommandStateContainer(DeviceNumber, MotorAngle, BallPosition) %#codegen

%skip size for now

Container = flip(typecast(int32(42), 'uint8')); %Device ID
Container = [Container flip(typecast(int32(DeviceNumber), 'uint8'))];
Container = [Container uint8(10)]; %Device function
Container = [Container flip(typecast(single(MotorAngle), 'uint8'))];
Container = [Container flip(typecast(single(BallPosition), 'uint8'))];

%Prepend container size
Container = [flip(typecast(int32(length(Container) + 4), 'uint8')) Container]';