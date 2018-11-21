function G = TemplateGraphGenerator(varargin)

%function to generate a template network that has the coloring properties
%of the network specified by baseLNLN

%example of input to the function
% nPerColor = [10 10 10 10 10 10 10 10];
% 
% 
% baseLNLN = [0 1 1 1 1 1 0 0;
%             1 0 1 1 1 0 1 0;
%             1 1 0 1 1 1 0 1;
%             1 1 1 0 1 0 1 0;
%             1 1 1 1 0 1 0 0;
%             1 0 1 0 1 0 0 0;
%             0 1 0 1 0 0 0 0;
%             0 0 1 0 0 0 0 0];

%default input
nPerColor = [10 5 10 10 10 10 10 10];
baseLNLN = [0 1 1 1 1 1 0 0;
            1 0 1 1 1 0 1 0;
            1 1 0 1 1 1 0 1;
            1 1 1 0 1 0 1 0;
            1 1 1 1 0 1 0 0;
            1 0 1 0 1 0 0 0;
            0 1 0 1 0 0 0 0;
            0 0 1 0 0 0 0 0];

if nargin > 0
    for jj = 1:2:length(varargin)-1
        name = varargin{jj};
        val = varargin{jj+1};
        
        eval([name, '= val;']);      

    end
end

    
nLN = sum(nPerColor); %number of neurons
nColors = length(nPerColor); %number of colors
m = max(nPerColor(:)); %max number of neurons in any group
tmp = ones(m); 
G = kron(baseLNLN,tmp);%generate base matrix

%now delete rows and columns to make the number of neurons associated with
%the ith color to ne nPercolor(i)
nDelete = m - nPerColor;
tmp = 1:m*nColors; tmp = reshape(tmp,m,nColors);
deleteRowsCols = [];
for ii = 1:size(baseLNLN,2)
    deleteRowsCols = [deleteRowsCols;tmp(1:nDelete(ii),ii)];
end
G(deleteRowsCols,:) = [];
G(:,deleteRowsCols) = [];
