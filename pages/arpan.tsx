import React, { useState } from 'react';
import { 
  BarChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend,
  ResponsiveContainer, LineChart
} from 'recharts';
import {
  AlertCircle,
  BarChart2,
  Hash,
  Link,
  Activity,
  Settings,
  Search,
  Calendar
} from 'lucide-react';

const TruthAIDashboard = () => {
  const [selectedTool, setSelectedTool] = useState('timeline');
  
  const timelineData = Array.from({ length: 30 }, (_, i) => ({
    date: `2024-01-${i + 1}`,
    posts: Math.floor(Math.random() * 10000) + 2000
  }));

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900">
      {/* Sidebar */}
      <div className="fixed left-0 top-0 h-full w-64 bg-gray-900 border-r border-gray-700">
        <div className="p-4">
          <h1 className="text-2xl font-bold text-purple-400">TruthAI</h1>
          
          <div className="mt-8">
            <div className="relative">
              <input
                type="search"
                placeholder="Search terms..."
                className="w-full bg-gray-800 border border-gray-700 rounded-lg pl-10 pr-4 py-2 text-gray-300"
              />
              <Search className="absolute left-3 top-2.5 h-5 w-5 text-gray-500" />
            </div>

            <div className="mt-4">
              <div className="flex items-center gap-2 mb-4">
                <Calendar className="h-5 w-5 text-gray-400" />
                <input
                  type="date"
                  className="bg-gray-800 border border-gray-700 rounded p-1 text-gray-300 text-sm"
                />
              </div>
            </div>

            <div className="space-y-2 mt-8">
              {[
                { icon: BarChart2, label: 'Timeline', id: 'timeline' },
                { icon: Hash, label: 'Hashtags', id: 'hashtags' },
                { icon: Link, label: 'Links', id: 'links' },
                { icon: Activity, label: 'Activity', id: 'activity' }
              ].map((tool) => (
                <button
                  key={tool.id}
                  onClick={() => setSelectedTool(tool.id)}
                  className={`w-full flex items-center gap-3 px-4 py-2 rounded-lg text-left ${
                    selectedTool === tool.id 
                      ? 'bg-purple-600 text-white' 
                      : 'text-gray-400 hover:bg-gray-800'
                  }`}
                >
                  <tool.icon className="h-5 w-5" />
                  {tool.label}
                </button>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="ml-64 p-8">
        <div className="grid grid-cols-4 gap-4 mb-8">
          {[
            { label: 'Active Monitors', value: '1,234', trend: '+12%' },
            { label: 'Flagged Content', value: '267', trend: '-5%' },
            { label: 'Total Sources', value: '892', trend: '+3%' },
            { label: 'Risk Score', value: '76%', trend: '+2%' }
          ].map((stat, i) => (
            <div key={i} className="bg-gray-800 rounded-lg p-4 border border-gray-700">
              <h3 className="text-gray-400 text-sm">{stat.label}</h3>
              <div className="mt-2 flex items-end justify-between">
                <span className="text-2xl font-bold text-white">{stat.value}</span>
                <span className={`text-sm ${
                  stat.trend.startsWith('+') ? 'text-green-400' : 'text-red-400'
                }`}>{stat.trend}</span>
              </div>
            </div>
          ))}
        </div>

        {/* Main Chart */}
        <div className="bg-gray-800 rounded-lg p-6 border border-gray-700 mb-8">
          <h2 className="text-xl font-bold text-white mb-6">Content Analysis</h2>
          <div className="h-96">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={timelineData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
                <XAxis dataKey="date" stroke="#9CA3AF" />
                <YAxis stroke="#9CA3AF" />
                <Tooltip 
                  contentStyle={{ backgroundColor: '#1F2937', border: '1px solid #374151' }}
                  labelStyle={{ color: '#9CA3AF' }}
                />
                <Legend />
                <Line 
                  type="monotone" 
                  dataKey="posts" 
                  stroke="#8B5CF6" 
                  strokeWidth={2}
                  dot={false}
                />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Bottom Section */}
        <div className="grid grid-cols-2 gap-8">
          <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
            <h2 className="text-xl font-bold text-white mb-4">Recent Alerts</h2>
            <div className="space-y-4">
              {[1, 2, 3].map((i) => (
                <div key={i} className="flex items-start gap-3 p-3 bg-gray-700/50 rounded-lg">
                  <AlertCircle className="h-5 w-5 text-red-400 mt-0.5" />
                  <div>
                    <h4 className="font-medium text-white">Potential Misinformation</h4>
                    <p className="text-sm text-gray-400">High engagement post detected with unverified claims</p>
                  </div>
                </div>
              ))}
            </div>
          </div>

          <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
            <h2 className="text-xl font-bold text-white mb-4">Top Sources</h2>
            <div className="space-y-4">
              {[1, 2, 3].map((i) => (
                <div key={i} className="flex items-center justify-between p-3 bg-gray-700/50 rounded-lg">
                  <div className="flex items-center gap-3">
                    <div className="h-8 w-8 rounded-full bg-purple-600/20 flex items-center justify-center">
                      <span className="text-purple-400 font-medium">{i}</span>
                    </div>
                    <div>
                      <h4 className="font-medium text-white">Source {i}</h4>
                      <p className="text-sm text-gray-400">Trust Score: {95 - i * 5}%</p>
                    </div>
                  </div>
                  <span className={`text-sm ${i === 1 ? 'text-green-400' : 'text-red-400'}`}>
                    {i === 1 ? '+12%' : '-' + (i * 3) + '%'}
                  </span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default TruthAIDashboard;