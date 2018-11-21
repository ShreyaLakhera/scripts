function G = GenerateDigraphFromTemplate(varargin)
%function to generate a directed graph from a template.
% inputs -- no inputs generate a default graph
%nPerColor = [10 10 10 10 10 10 10 10]; %number of neurons associated with
%each color
% 
% base graph
% baseLNLN = [0 1 1 1 1 1 0 0;
%             1 0 1 1 1 0 1 0;
%             1 1 0 1 1 1 0 1;
%             1 1 1 0 1 0 1 0;
%             1 1 1 1 0 1 0 0;
%             1 0 1 0 1 0 0 0;
%             0 1 0 1 0 0 0 0;
%             0 0 1 0 0 0 0 0];
% \
% directed arcs of the graph
% baseAdjList =  [1,2;
%                 2,3;
%                 3,4;
%                 4,5]
% probability of connections bein unidirectional
% pConn = [0.8;
%         0.8;
%         0.8;
%         0.8];
% 
%output G

%default inputs
nPerColor = [10 10 10 10 10 10 10 10];

baseLNLN = [0 1 1 1 1 1 0 0;
            1 0 1 1 1 0 1 0;
            1 1 0 1 1 1 0 1;
            1 1 1 0 1 0 1 0;
            1 1 1 1 0 1 0 0;
            1 0 1 0 1 0 0 0;
            0 1 0 1 0 0 0 0;
            0 0 1 0 0 0 0 0];

baseAdjList =  [1,2;
                2,3;
                3,4;
                4,5]
pConn = [0.8;
        0.8;
        0.8;
        0.8];
    
if nargin > 0
    for jj = 1:2:length(varargin)-1
        name = varargin{jj};
        val = varargin{jj+1};
        
        eval([name, '= val;']);      

    end
end
    
G = TemplateGraphGenerator('nPerColor',nPerColor,'baseLNLN',baseLNLN);

for ii = 1:size(baseAdjList,1)
    %determine which block to delete connections from
    in = baseAdjList(ii,2);
    out = baseAdjList(ii,1);
    r = [sum(nPerColor(1:in-1))+1,sum(nPerColor(1:in))]
    c = [sum(nPerColor(1:out-1))+1,sum(nPerColor(1:out))]
    
    rnum = rand(diff(r)+1,diff(c)+1);
    rnum = double(rnum > pConn(ii));
    G(r(1):r(2),c(1):c(2)) = rnum.*G(r(1):r(2),c(1):c(2));
end