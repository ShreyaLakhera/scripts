%script to write a synapse.isf file

%% Generate connectivity matrix
nPerColor = [3 3 3 3]; %number of neurons per color group
nNeurons = sum(nPerColor);
graphTemplate = [0 1 1 1;
                 1 0 1 1;
                 1 1 0 1;
                 1 1 1 0];
C = TemplateGraphGenerator('nPerColor',nPerColor,'baseLNLN',graphTemplate);             
[pre,post] = find(C);
nSynapses = length(pre); %number of synapses
pre = pre -1;
post = post -1; %convert indices to zero based for c++

%% synapse variables
gij = 1/9*2; %synaptic weight

var{1} = 'dxdt';
val{1} = zeros(nSynapses,1);

var{2} = 'pre';
val{2} = pre;

var{3} = 'post';
val{3} = post;

var{4} = 'threshold';
val{4} = zeros(nSynapses,1);

var{5} = 'g_syn';
ind = sub2ind([nNeurons,nNeurons],pre+1,post+1);
val{5} = gij*C(ind);

var{6} = 'inp';
val{6} = zeros(nSynapses,1);

%% write the variables to a text file
pathname = '/data/models2/RabinovichPRL/networks/coloredGraphs';
filename = 'ssets.isf'
fid = fopen(fullfile(pathname,filename),'w');


for ii = 1:nSynapses
    tmp = ['synapse ',int2str(ii-1),' : neuron',int2str(pre(ii)-1),'---> neuron',int2str(post(ii)-1)];
    comment(fid,tmp);
    endoffile = 0;
    
    for jj = 1:length(var)
        if jj == 2
            comment(fid,'parameters')
        end
        
        if jj == 6
            comment(fid,'synaptic current to observe')
        end
        
        if jj == length(var);
            endoffile = 1;
        end
        var_val_comment(fid,var{jj},val{jj}(ii),endoffile);
    end
    drawline(fid,40);
end