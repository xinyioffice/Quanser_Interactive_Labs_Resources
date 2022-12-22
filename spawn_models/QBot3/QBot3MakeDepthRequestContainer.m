function Container = QBot3MakeDepthRequestContainer(DeviceNumber) %#codegen

%skip size for now

Container = flip(typecast(int32(22), 'uint8')); %Device ID
Container = [Container flip(typecast(int32(DeviceNumber), 'uint8'))];
Container = [Container uint8(110)]; %Device function
%No payload

%Prepend container size
Container = [flip(typecast(int32(length(Container) + 4), 'uint8')) Container]';