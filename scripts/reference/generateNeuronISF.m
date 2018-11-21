%script to generate a neuron.isf file
nNeurons = 12;
%variables and values for the neurons
var{1} = 'dxdt';
val{1} = 3*ones(nNeurons,1);

var{2} = 'x';
val{2} = rand(nNeurons,1);

var{3} = 'y';
val{3} = rand(nNeurons,1);

var{4} = 'z';
val{4} = rand(nNeurons,1);

var{5} = 'nu';
val{5} = -1.5*ones(nNeurons,1);

var{6} = 'a';
val{6} = 0.7*ones(nNeurons,1);

var{7} = 'b';
val{7} = 0.8*ones(nNeurons,1);

var{8} = 'tau1';
val{8} = 0.08*ones(nNeurons,1);

var{9} = 'tau2';
val{9} = 4.1*ones(nNeurons,1);

var{10} = 'dc';
val{10} = 0.35*ones(nNeurons,1);

var{11} = 'I_ext';
a = 0; b = 0.002;
r = a + (b-a)*rand(nNeurons,1);
val{11} = 0.01*ones(nNeurons,1) + r;

var{12} = 'I_syn';
val{12} = zeros(nNeurons,1);

%write the variables to a text file
pathname = '../RabinovichPRL/networks/coloredGraphs';
filename = 'nsets.isf'
fid = fopen(fullfile(pathname,filename),'w');



for ii = 1:nNeurons
    endoffile = 0;
    tmp = ['neuron ',int2str(ii-1)]
    comment(fid,tmp);
    
    for jj = 1:length(var) 
        
        %insert comments
        if jj == 5
            comment(fid,'parameters')
        end
        
        if jj == 12
            comment(fid,'Currents to observe')
        end
        
        if jj == length(var);
            endoffile = 1;
        end
        
        var_val_comment(fid,var{jj},val{jj}(ii),endoffile);
    end
    drawline(fid,40);
end
fclose(fid);
